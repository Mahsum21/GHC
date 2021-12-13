from django.db.models import fields
from django.forms import TextInput, EmailInput, NumberInput, DateInput, widgets
from django.forms.models import ModelForm
from models import *    

class MatiereForm(ModelForm):
    class meta: 
        model = Matiere
        fields= ["nom", "dureeTotal"]
        widgets={
            'nom': TextInput(attrs={'class':'form-control'})
        }

class HoraireForm(ModelForm)