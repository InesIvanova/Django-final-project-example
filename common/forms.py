from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ('image',)