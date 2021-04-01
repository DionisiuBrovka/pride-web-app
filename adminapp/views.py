from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import *
from data.forms import *
from adminapp.alghorytm import random_string


def user_permission_check(user):
    if (user.is_authenticated):
        if (user.is_staff):
            return False
    return True

# Create your views here.
def index(request):
    return render(request, 'adminapp/index.html')


# ====================================================================================
# ====================================================================================
# ====================================================================================
def pg_users(request):
    user = request.user

    if user_permission_check(user):
        return redirect('autherror')
        

    data = {
        'user':user,
        'users':Profile.objects.all(),
        'form':ProfileForm(),
    }
    return render(request, 'adminapp/user/pg_users.html', data)

def pg_user(request, pk=1):
    user = request.user

    if user_permission_check(user):
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

    if user_permission_check(user):
        return redirect('autherror')

    if request.method == "POST":
        newProfileForm = ProfileForm(request.POST, request.FILES)
        newMobileForm = MobileForm(request.POST)
        if newProfileForm.is_valid() and newMobileForm.is_valid():
            newProfile = Profile.objects.get(user__id=pk)
            newProfile.name = newProfileForm.cleaned_data['name']
            newProfile.famName = newProfileForm.cleaned_data['famName']
            newProfile.fathName = newProfileForm.cleaned_data['fathName']
            newProfile.vk = newProfileForm.cleaned_data['vk']
            newProfile.telegramNick = newProfileForm.cleaned_data['telegramNick']
            newProfile.avatar = newProfileForm.cleaned_data['avatar']
            newProfile.trainee = newProfileForm.cleaned_data['trainee']
            newProfile.save()
            newMobile = MobilePhone.objects.filter(staff = Profile.objects.get(user__id=pk))
            newMobile.number = newMobileForm.cleaned_data['number']
            newMobile.save()

    data = {
        'user':user,
        'profileForm':ProfileForm(),
        'mobileForm':MobileForm(),
        'profile':Profile.objects.get(user__id=pk),
        'mobile':MobilePhone.objects.filter(staff__user__id=pk),
    }

    return render(request, 'adminapp/user/pg_user_edit.html', data)

def pg_add_user(request):
    user = request.user

    if user_permission_check(user):
        return redirect('autherror')
    
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

    if user_permission_check(user):
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

    if user_permission_check(user):
        return redirect('autherror')

    if request.method == "POST":
        newPlaceForm = PlaceForm(request.POST, request.FILES)
        newIBANForm = IBANForm(request.POST)
        if newPlaceForm.is_valid() and newIBANForm.is_valid():
            newPlace = newPlaceForm.save(commit=False)
            newPlace.save()
            newIBAN = newIBANForm.save(commit=False)
            newIBAN.place = newPlace
            newIBAN.save()

    data = {
        'user':user,
        'placeForm':PlaceForm(),
        'ibanForm':IBANForm(),
    }
    return render(request, 'adminapp/place/pg_place_add.html', data)

def pg_place_edit(request, pk=1):
    user = request.user

    curPlace = Place.objects.get(id=pk)

    if user_permission_check(user):
        return redirect('autherror')

    if request.method == "POST":
        newPlaceForm = PlaceForm(request.POST, request.FILES)
        if newPlaceForm.is_valid() and request.POST.get('ActionType') == "Edit":
            newPlace = Place.objects.get(id = pk)
            newPlace.title = newPlaceForm.cleaned_data['title']
            newPlace.preview = newPlaceForm.cleaned_data['preview']
            newPlace.adres = newPlaceForm.cleaned_data['adres']
            newPlace.percentForPlace = newPlaceForm.cleaned_data['percentForPlace']
            newPlace.percentForWorker = newPlaceForm.cleaned_data['percentForWorker']
            newPlace.govTitle = newPlaceForm.cleaned_data['govTitle']
            newPlace.unp = newPlaceForm.cleaned_data['unp']
            newPlace.govAdress = newPlaceForm.cleaned_data['govAdress']
            newPlace.bankcode = newPlaceForm.cleaned_data['bankcode']
            newPlace.save()
        if request.POST.get('ActionType') == "add":
            newIBANForm = IBANForm(request.POST)
            if newIBANForm.is_valid():
                newIBAN = newIBANForm.save(commit=FALSE)
                newIBAN.place = curPlace
                newIBAN.save()
        if (request.POST.get('ActionType') != "add") and request.POST.get('ActionType') != "Edit":
            newIBAN = IBAN.objects.get(id = request.POST.get('ActionType'))
            newIBAN.delete()


    data = {
        'user':user,
        'place':curPlace,
        'iban':IBAN.objects.filter(place=curPlace),
        'placeForm':PlaceForm(),
        'ibanForm':IBANForm(),
    }
    return render(request, 'adminapp/place/pg_place_edit.html', data)

# ====================================================================================
# ====================================================================================
# ====================================================================================
def pg_sessions(request):
    user = request.user

    if user_permission_check(user):
        return redirect('autherror')
    
    sessions = Session.objects.all().order_by("-startTime")

    data = {
        'user':user,
        'sessions':sessions,
    }
    return render(request, 'adminapp/session/pg_sessions.html', data)

def pg_session_edit(request, pk=1):
    user = request.user

    if user_permission_check(user):
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

    if user_permission_check(user):
        return redirect('autherror')

    items = Item.objects.all()

    data = {
        'user':user,
        'items':items,        
    }
    return render(request, 'adminapp/item/pg_items.html', data)

def pg_item(request, pk=1):
    user = request.user

    if user_permission_check(user):
        return redirect('autherror')

    items = Item.objects.all()

    data = {
        'user':user,
        'items':items,    
        'form':Rec    
    }
    return render(request, 'adminapp/item/pg_item.html', data)

def pg_item_edit(request, pk=1):
    user = request.user

    if user_permission_check(user):
        return redirect('autherror')

    data = {
        'user':user,
        'item':Item.objects.get(id=pk),
    }
    return render(request, 'adminapp/item/pg_item_edit.html', data)

def pg_items_add(request):
    user = request.user

    if user_permission_check(user):
        return redirect('autherror')

    

    data = {
        'user':user,
    }
    return render(request, 'adminapp/item/pg_item_add.html', data)
