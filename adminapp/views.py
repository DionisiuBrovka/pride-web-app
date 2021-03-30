from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import Profile, Place, Session, Recvisites, MobilePhone, StartSession, EndSession, AddToSession, DeleteOnSession, Item
from data.forms import ProfileForm
from adminapp.alghorytm import random_string

# Create your views here.
def index(request):
    return render(request, 'adminapp/index.html')


# ====================================================================================
# ====================================================================================
# ====================================================================================
def pg_users(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    data = {
        'user':user,
        'users':Profile.objects.all(),
        'form':ProfileForm(),
    }
    return render(request, 'adminapp/user/pg_users.html', data)

def pg_user(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    selectUser = Profile.objects.get(id=pk)
    selectUserSessions = Session.objects.filter(staff__id=pk)
    selectUserPhones = MobilePhone.objects.filter(staff__id=pk)

    data = {
        'user':user,
        'selectUser':selectUser,
        'selectUserSessions':selectUserSessions,
        'selectUserPhones':selectUserPhones,
    }

    return render(request, 'adminapp/user/pg_user.html', data)

def pg_user_edit(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    data = {
        'user':user,
    }

    return render(request, 'adminapp/user/pg_user_edit.html', data)

def pg_add_user(request):
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
    return render(request, 'adminapp/user/pg_add_user.html',data)

# ====================================================================================
# ====================================================================================
# ====================================================================================
def pg_places(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    data = {
        'user':user,
        'places':Place.objects.all(),
    }
    return render(request, 'adminapp/place/pg_places.html', data)

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
    return render(request, 'adminapp/place/pg_place.html', data)

def pg_place_add(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    data = {
        'user':user,
    }
    return render(request, 'adminapp/place/pg_place_add.html', data)

def pg_place_edit(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    data = {
        'user':user,
    }
    return render(request, 'adminapp/place/pg_place_edit.html', data)

# ====================================================================================
# ====================================================================================
# ====================================================================================
def pg_sessions(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    sessions = Session.objects.all().order_by("-startTime")

    data = {
        'user':user,
        'sessions':sessions,
    }
    return render(request, 'adminapp/session/pg_sessions.html', data)

def pg_session(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    curSession = Session.objects.get(id = pk)
    itemsInit = StartSession.objects.filter(session = curSession)
    itemsEnd = EndSession.objects.filter(session=curSession)
    itemsAdd = AddToSession.objects.filter(session=curSession)
    itemsDec = DeleteOnSession.objects.filter(session=curSession)

    data = {
       'user':user,
       'session':curSession,
       'itemsInit':itemsInit,
       'itemsEnd':itemsEnd,
       'itemsAdd':itemsAdd,
       'itemsDec':itemsDec,
    }
    return render(request, 'adminapp/session/pg_session.html', data)

def pg_session_add(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    sessions = Session.objects.all().order_by("-startTime")

    data = {
        'user':user,
        'sessions':sessions,
    }
    return render(request, 'adminapp/session/pg_sessions_add.html', data)

def pg_session_edit(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')
    
    sessions = Session.objects.all().order_by("-startTime")

    data = {
        'user':user,
        'sessions':sessions,
    }
    return render(request, 'adminapp/session/pg_sessions_edit.html', data)

# ====================================================================================
# ====================================================================================
# ====================================================================================
def pg_items(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    items = Item.objects.all()

    data = {
        'user':user,
        'items':items,        
    }
    return render(request, 'adminapp/item/pg_items.html', data)

def pg_item(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    items = Item.objects.all()

    data = {
        'user':user,
        'items':items,        
    }
    return render(request, 'adminapp/item/pg_item.html', data)

