from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import Profile, Place, Session, Recvisites
from data.forms import ProfileForm

# Create your views here.
def index(request):
    return render(request, 'adminapp/index.html')

def pg_users(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    data = {
        'user':user,
        'users':Profile.objects.all(),
        'form':ProfileForm(),
    }
    return render(request, 'adminapp/pg_users.html', data)

def pg_user(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    selectUser = Profile.objects.get(id=pk)
    selectUserSessions = Session.objects.filter(staff__id=pk)

    data = {
        'user':user,
        'selectUser':selectUser,
        'selectUserSessions':selectUserSessions,
    }

    return render(request, 'adminapp/pg_user.html', data)

def pg_places(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    data = {
        'places':Place.objects.all()
    }
    return render(request, 'adminapp/pg_places.html', data)

def pg_place(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    selectPlace = Place.objects.get(id=pk)
    selectPlaceSessions = Session.objects.filter(place__id=pk)

    data = {
        'user':user,
        'selectPlace':selectPlace,
        'selectPlaceSessions':selectPlaceSessions,
    }
    return render(request, 'adminapp/pg_place.html', data)

def pg_sessions(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    data = {
        'user':user,
    }
    return render(request, 'adminapp/pg_sessions.html', data)

def pg_session(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    data = {
        'user':user,
    }
    return render(request, 'adminapp/pg_session.html', data)