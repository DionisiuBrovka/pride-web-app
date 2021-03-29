from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="adminapp"),
    path('users/', views.pg_users, name = "adminapp-users"),
    path('user/<int:pk>/', views.pg_user, name="adminapp-user"),
    path('places/', views.pg_places, name = "adminapp-places"),
    path('place/<int:pk>/', views.pg_place, name="adminapp-place"),
    path('sessions/', views.pg_sessions, name = "adminapp-sessions"),
    path('session/<int:pk>/', views.pg_session, name="adminapp-session"),
]