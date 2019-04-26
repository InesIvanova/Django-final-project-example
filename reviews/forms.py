from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Review


class ReviewForm(forms.Form):

    # author = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #     }
    # ))

    score = forms.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)] ,widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Review
        fields = ('score', 'content')