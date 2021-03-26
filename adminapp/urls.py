from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="adminapp"),
    path('users/', views.pg_users, name = "users"),
    path('user/<int:pk>/', views.pg_user, name="user"),
    path('places/', views.pg_places, name = "places"),
]