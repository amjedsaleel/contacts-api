# django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    picture = models.ImageField(blank=True)
    country_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)


