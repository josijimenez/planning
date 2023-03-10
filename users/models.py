from django.db import models
#-----
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from eods.models import Eod

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=100)
    identification = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10)

    eod = models.ForeignKey(Eod, on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un Usuario pertenece a una sola Eod, pero la misma Eod puede tener muchos usuarios.

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    REQUIRED_FIELDS = ['role', 'identification']

    objects = UserManager()

    def __str__(self):
        return self.email