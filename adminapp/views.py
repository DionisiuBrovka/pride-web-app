from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import Profile, Place
from data.forms import ProfileForm

# Create your views here.
def index(request):
    return render(request, 'adminapp/index.html')

def pg_users(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    data = {
        'users':Profile.objects.all(),
        'form':ProfileForm(),
    }
    return render(request, 'adminapp/pg_users.html', data)

def pg_places(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    data = {
        'places':Place.objects.all()
    }
    return render(request, 'adminapp/pg_places.html', data)