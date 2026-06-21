from django.urls import path
from car import views

urlpatterns = [
    path('',views.get_cars,name='list'),
    path('create_car/', views.create_car, name='create_car'),
    path('read_car/<int:pk>/', views.read_car, name='read_car'),
]