from django.shortcuts import render,get_object_or_404,redirect
from collec_management.models import Collec
from collec_management.forms import CollecForm
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.utils import timezone
from .models import Element
from .forms import ElementForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    return render(request,"collec_management/about.html")

def collections_details(request, collection_id):
    # Récupérer la collection par son ID
    collection = get_object_or_404(Collec, pk=collection_id)
    
    # Récupérer les éléments associés à cette collection
    elements = Element.objects.filter(collection=collection)
    
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.collection = collection
            element.date=timezone.now()
            element.save()
            return redirect('collections_details', collection_id=collection.id)
    else:
        form = ElementForm(initial={'collection': collection.pk})
    
    return render(request, 'collec_management/collections_details.html', {
        'collection': collection,
        'elements': elements,
        'form': form
    })
@login_required
def collections_list(request):
    collections = Collec.objects.all().order_by('-date')
    return render(request, 'collec_management/collections_list.html', {'collections': collections})

@login_required
def new_collection(request):
    if request.method == "POST":
        form = CollecForm(request.POST)
        if form.is_valid():
            collec = form.save(commit=False)
            collec.date = timezone.now().date()
            collec.save()

        return HttpResponseRedirect(f"/collection/{collec.id}")
    else:
        form = CollecForm()  # Formulaire vide

    return render(request, "collec_management/add_collection.html", {"form": form})

def delete_collection(request, collection_id):
    collection = get_object_or_404(Collec, id=collection_id)
    if request.method == 'POST': 
        collection.delete()
        return redirect('collections_list') # Redirige vers la liste des collections après suppression 
    
    return render(request, 'collec_management/delete_collection.html', {'collection': collection})

def edit_collection(request, collection_id):
    collection = get_object_or_404(Collec, id=collection_id)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/collection/{collection.id}")
    else:
        form = CollecForm(instance=collection)

    return render(request, 'collec_management/edit_collection.html', {'form': form})

def home(request):
    return render(request, 'collec_management/home.html')

def add_element(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            element=form.save(commit=False)
            element.date=timezone.now()
            element.save()
            return HttpResponseRedirect(f"/collection/{element.collection.pk}")
    else:
        form = ElementForm()
    return render(request, 'collec_management/element_add.html', {'form': form})


def delete_element(request, pk):
    element = get_object_or_404(Element, pk=pk)
    if request.method == 'POST':
        element.delete()
        
        return HttpResponseRedirect(f"/collection/{element.collection.pk}")
    return render(request, 'collec_management/element_delete.html', {'element': element}) 

def element_details(request, pk):
    element = get_object_or_404(Element, pk=pk)
    return render(request, 'collec_management/element_details.html', {'element': element})

def edit_element(request, pk):
    element = get_object_or_404(Element, pk=pk)

    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            return redirect('element_details', pk=element.pk)
    else:
        form = ElementForm(instance=element)

    return render(request, 'collec_management/element_edit.html', {'form': form, 'element': element})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'collec_management/login.html')

def custom_logout(request):
    logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect('home')