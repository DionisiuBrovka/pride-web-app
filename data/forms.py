from django.forms import ModelForm
from .models import *

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'adres', 'preview','unp','govAdress','bankcode','govTitle']

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['place']

class StratSessionForm(ModelForm):
    class Meta:
        model = StartSession
        fields = ['count']

class AddToSessionForm(ModelForm):
    class Meta:
        model = AddToSession
        fields = ['item', 'count']

class EndSessionForm(ModelForm):
    class Meta:
        model = EndSession
        fields = ['count']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['position','comment']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName','secondName','thirdName','vk','telegramNick','avatar']

class DamageForm(ModelForm):
    class Meta:
        model = Damage
        fields = ['image', 'comment']

class DraftForm(ModelForm):
    class Meta:
        model = Draft
        fields = ['image','comment']

class AddedCostForm(ModelForm):
    class Meta:
        model = AddedCost
        fields = ['image', 'comment', 'cost']

class IBANForm(ModelForm):
    class Meta:
        model = IBAN
        fields = ['title','iban']

class MobileForm(ModelForm):
    class Meta:
        model = MobilePhone
        fields = ['number']