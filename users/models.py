from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class CustomAccountManager(BaseUserManager):
  
  def create_superuser(self, email, first_name, password, **other_fields):

    other_fields.setdefault('is_staff', True)
    other_fields.setdefault('is_superuser', True)
    other_fields.setdefault('is_active', True)

    if other_fields.get('is_staff') is not True:
      raise ValueError('Superuser must be assigned to is_staff=True.')
    if other_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must be assigned to is_superuser=True.')
    
    return self.create_user(email, first_name, password, **other_fields)
  
  def create_user(self, email, first_name, password, **other_fields):

    if not email:
      raise ValueError(_('You must provide an email address'))

    email = self.normalize_email(email)
    user = self.model(email=email, first_name=first_name, **other_fields)
    user.set_password(password)
    preint(password)
    user.save()
    return user

class NewUser(AbstractBaseUser, PermissionsMixin):

  email = models.EmailField(_('email address'), unique=True)
  first_name = models.CharField(max_length=150, blank=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  objects = CustomAccountManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name']

  def __str__(self):
    return self.first_name