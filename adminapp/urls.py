from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="adminapp"),
    path('users/', views.pg_users, name = "adminapp-users"),
    path('user/<int:pk>/', views.pg_user, name="adminapp-user"),
    path('users/add', views.pg_add_user, name = "adminapp-adduser"),
    path('user/<int:pk>/edit', views.pg_user_edit, name="adminapp-user-edit"),

    path('places/', views.pg_places, name = "adminapp-places"),
    path('place/<int:pk>/', views.pg_place, name="adminapp-place"),
    path('places/add', views.pg_place_add, name = "adminapp-places-add"),
    path('place/<int:pk>/edit', views.pg_place_edit, name="adminapp-place-edit"),

    path('sessions/', views.pg_sessions, name = "adminapp-sessions"),
    path('session/<int:pk>/edit', views.pg_session_edit, name="adminapp-session-edit"),

    path('items/', views.pg_items, name="adminapp-items"),
    path('item/<int:pk>/', views.pg_item, name="adminapp-item"),
    path('items/add', views.pg_items_add, name="adminapp-items-add"),
    path('item/<int:pk>/edit', views.pg_item_edit, name="adminapp-item-edit"),
]