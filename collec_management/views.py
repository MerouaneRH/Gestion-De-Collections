from django.shortcuts import render,get_object_or_404
from collec_management.models import Collec
from collec_management.forms import CollecForm
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.utils import timezone

# Create your views here.

def about(request):
    return render(request,"collec_management/about.html")

def collections_details(request, collection_id):
    collection = get_object_or_404(Collec, pk=collection_id)
    return render(request, 'collec_management/collections_details.html', {'collection': collection})

def collections_list(request):
    collections = Collec.objects.all().order_by('-date')
    return render(request, 'collec_management/collections_list.html', {'collections': collections})

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
