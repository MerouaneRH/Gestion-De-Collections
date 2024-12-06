
from collec_management import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/<int:collection_id>/', views.collections_details, name='collections_details'),
    path('all/', views.collections_list, name='collections_list'),
    path('new/', views.new_collection, name='new_collection'),
    path('delete/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('change/<int:collection_id>/', views.edit_collection,name='edit_collection'),
    path('element/add', views.add_element, name='add_element'),
    path('element/delete/<int:pk>/', views.delete_element, name='delete_element'),
    path('element/<int:pk>/', views.element_details, name='element_details'),
    path('element/edit/<int:pk>/', views.edit_element, name='edit_element'),

]
