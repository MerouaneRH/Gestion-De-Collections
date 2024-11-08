from django.shortcuts import render,get_object_or_404
from collec_management.models import Collec

# Create your views here.

def about(request):
    return render(request,"collec_management/about.html")

def collections_details(request, collection_id):
    collection = get_object_or_404(Collec, pk=collection_id)
    return render(request, 'collec_management/collections_details.html', {'collection': collection})

def collections_list(request):
    collections = Collec.objects.all().order_by('-date')
    return render(request, 'collec_management/collections_list.html', {'collections': collections})
