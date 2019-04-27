from django import forms
from django.core.validators import MinValueValidator

from .models import Furniture, Material


class MaterialForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-contol'
        }
    ))

    class Meta:
        model = Material
        fields = ('name',)


class CreateFurnitureForm(forms.ModelForm):

    make = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    model = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True ,widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    price = forms.IntegerField(required=True,
                            validators=[MinValueValidator(10)],
                            widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    material = forms.ModelChoiceField(queryset=Material.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control'
                                          }
                                      ))


    class Meta:
        model = Furniture
        fields = ('id', 'make', 'model', 'description', 'price', 'image_url', 'material')