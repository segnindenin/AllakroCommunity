from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models

# class MyActeurForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = ('username', 'statut', 'HabitantID', 'password1', 'password2')

class MyActeurForm(UserCreationForm):
    HabitantID = forms.CharField(required=False)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'statut', 'password1', 'password2')
    # def clean_HabitantID(self):
    #     HabitantID = self.cleaned_data.get('HabitantID')
    #     if HabitantID:
    #         try:
    #             habitant = models.Habitant.objects.get(id=HabitantID)
    #         except models.Habitant.DoesNotExist:
    #             raise forms.ValidationError("L'élément lié n'existe pas. Veuillez saisir un élément valide.")
    #         return habitant
    #     else:
    #         return None

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class HabitantForm(ModelForm):
    class Meta:
        model = models.Habitant
        fields = '__all__'


class ActivityForm(ModelForm):
    class Meta:
        model = models.Activity
        fields = ['objet', 'publication', 'communityID']


class CommunautyForm(ModelForm):
    class Meta:
        model = models.Communauty
        fields = ['name', 'categorie', 'localisation', 'service']


class CarnetSanteForm(ModelForm):
    class Meta:
        model = models.CarnetSante
        fields = '__all__'


class JobOffer(ModelForm):
    class Meta:
        model = models.JobOffer
        fields = '__all__'


class PostulationForm(ModelForm):
    class Meta:
        model = models.Postulation
        fields = '__all__'


class ProjetForm(ModelForm):
    class Meta:
        model = models.Projet
        fields = ['name', 'state', 'description', 'startDate', 'endDate', 'communityID']
