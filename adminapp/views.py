from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import Profile, Place, Session, Recvisites
from data.forms import ProfileForm
from adminapp.alghorytm import random_string

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

def pg_add_user(request)
    AddedUser = {}

    if (request.method == "POST"):
        newProfile = ProfileForm(request.POST)
        if newProfile.is_valid():
            newUser = auth.models.User(
                username = random_string.get_random_string(5),
                password = random_string.get_random_string(10),
            )
            newUser.save()
            userProfile = Profile.objects.get(user=newUser)
            userProfile.name = newProfile.cleaned_data['name']
            userProfile.famName = newProfile.cleaned_data['famName']
            userProfile.fathName = newProfile.cleaned_data['fathName']
            userProfile.vk = newProfile.cleaned_data['vk']
            userProfile.avatar = newProfile.cleaned_data['avatar']
            userProfile.telegramNick = newProfile.cleaned_data['telegramNick']
            userProfile.save()
            print (newUser.username)
            print (newUser.password)
            AddedUser = {
                'login':newUser.username,
                'password':newUser.password,
            }
            

    data = {
        'form':ProfileForm(),
        'newUser':AddedUser,
    }
    return render(request, 'adminapp/pg_add_user.html',data)
