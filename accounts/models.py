from django.db import models
# Create your models here.
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    # creating normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name  = last_name, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #  creating superuser
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name  = last_name,
            
        )
        user.is_admin =True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name  = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    username  = models.CharField(max_length=50, unique=True)
    email  = models.EmailField(max_length=50, unique=True)
    password  = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, default="0722247453")

    # required fields
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin =models.BooleanField(default=True)
    is_staff =models.BooleanField(default=True)
    is_active =models.BooleanField(default=True)
    is_superadmin =models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    objects = MyAccountManager()
    def __str__(self):
        return self.email

    def has_perm(self, prem, obj=None):
        return self.is_admin
        
    def has_module_perms(self,add_lebel):
        return True