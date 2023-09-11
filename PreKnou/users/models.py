from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

# this class provides functionalites to create an ordinary user and a superuser
class CustomUserManager(BaseUserManager):
    #extra_fields create room for additional fields
    def create_user(self, email, password=None, **extra_fields):
        #handling email exceptions
        if not email:
            raise ValueError(_('The email field must set'))
        
        #behaviors a user can have while creating an account
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, passowrd=None, **extra_fields):
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_stuff') is False:
            raise ValueError(_('Superuser is_stuff=True'))
        
        if extra_fields.get('is_superuser') is False:
            raise ValueError(_('Superuser is_superuser=True'))
        
        return self.create_user(email, passowrd, **extra_fields)

class UserCustomization(AbstractBaseUser, PermissionsMixin):
    
    #setting fields for our form
    first_name = models.CharField(_('First name'), max_length=30)
    last_name = models.CharField(_('Last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True, max_length=60)
    date_of_birth = models.DateField(_('Date of birth'))
    is_active = models.BooleanField(_('is active'), default=True)
    is_stuff = models.BooleanField(_('is stuff'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']
    
    def __str__(self):
        self.first_name
    
        