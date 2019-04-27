from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

from accounts.models import ProfileUser
# Create your models here.


class Material(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Furniture(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    image_url = models.URLField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.user} has {self.make}"





