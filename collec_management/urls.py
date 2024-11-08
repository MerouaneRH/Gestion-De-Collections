
from collec_management import views
from django.urls import path

urlpatterns = [
    path('about/', views.about, name='about'),
    path('collection/<int:collection_id>/', views.collections_details, name='collections_details'),
    path('all/', views.collections_list, name='collections_list'),
    path('new/', views.new_collection, name='new_collection'),
    path('delete/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('change/<int:collection_id>/', views.edit_collection,name='edit_collection'),


]
