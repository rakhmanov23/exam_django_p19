from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/', blank=True)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=25)
