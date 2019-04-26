from django.db import models

from accounts.models import ProfileUser
from furnitures.models import Furniture
# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField()
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)