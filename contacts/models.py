from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


user = get_user_model()


class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="Аватар"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.secondname} - {self.phone_number}"
