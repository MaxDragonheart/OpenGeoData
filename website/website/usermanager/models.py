from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class UserProfile(AbstractUser):
    """
    UserProfile inherits AbstractUser, it is used to
    create a website user.
    """
    name = models.CharField(max_length=75, blank=True)
    surname = models.CharField(max_length=75, blank=True)
    email = models.EmailField(max_length=75, blank=True)

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return str(self.name) + ' ' + str(self.surname)

    def get_absolute_url(self):
        return reverse("user_details", kwargs={"username":self.username})

    class Meta:
        ordering = ['username']
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profile"