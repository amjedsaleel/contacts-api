# django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def get_picture_upload_path(self):
    """
    It returns dynamic upload path for picture field in  Contact model,
    Based on logged user
    """
    return f'{self.user.username}/{"profile.png"}'


class Contact(models.Model):
    """
    Defines the fields for saving contacts of user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    picture = models.ImageField(upload_to=get_picture_upload_path, blank=True)
    country_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)
