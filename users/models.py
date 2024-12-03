from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='users/profile_images/')
    
    def __str__(self):
        return self.username
