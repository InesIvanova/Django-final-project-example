from django.db import models

from .enums import TestEnum
# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='images/')


class Dummy(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in TestEnum])

    def __str__(self):
        return f"{self.name} {self.get_color_display()}"