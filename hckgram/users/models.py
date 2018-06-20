from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):


    #User Models
    # First Name and Last Name do not cover name patterns
    # around the globe.
    GENDER_CHOICE = (
        ('male','Male'),
        ('female','Female'),
        ('not','Not')
    )

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=140,null=True)
    gender = models.CharField(max_length=80,choices = GENDER_CHOICE,null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})