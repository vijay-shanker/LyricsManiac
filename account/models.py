from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __unicode__(self):
        return self.get_full_name()
        
    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]) or self.username
    
    def get_short_name(self):
        return self.first_name or self.username
    

    
    
    
    