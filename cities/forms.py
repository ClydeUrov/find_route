from django import forms
from django.forms import ModelForm, Form
from cities.models import City


class HtmlForm(Form):
    name = forms.CharField(label="Город")

class CityForm(ModelForm):
    name = forms.CharField(label="Город", widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Введите название города',
    }))
    class Meta:
        model = City
        fields = ('name',)