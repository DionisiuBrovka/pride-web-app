from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('', views.index, name="index"),
    path('404/', views.view_error404, name="404"),
    path('500/', views.view_error500, name="500"),
]