from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, who_r_u,password):
        if not email:
            raise ValueError("Valid Email Required !")
        if not username:
            raise ValueError("Valid username Required !")

        user = self.model( 
            email = self.normalize_email(email),
            who_r_u=who_r_u,
            username=username,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, who_r_u,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            who_r_u=who_r_u,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True 
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(verbose_name='User name',max_length=30,unique=True)
    email = models.EmailField(verbose_name='Email', max_length=60,unique=True)
    date_joined = models.DateField(verbose_name='Date Joined',auto_now_add=True)
    date_login = models.DateField(verbose_name='Last Login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    OPTIONS=(
        (0,'not sure why am here'),
        (1,'Student'),
        (2,'Faculty'),
        (3,'Admin'),
    )
    who_r_u = models.SmallIntegerField(choices = OPTIONS, null=False, verbose_name='Who r u field !')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','who_r_u']

    objects = MyAccountManager()

    def save(self, *args, **kwargs):
        
        if self.who_r_u == 3:
            self.is_staff = True
            self.is_admin = True
        if self.who_r_u == 2:
            self.is_staff = True
        return super(Account, self).save()

    def __str__(self):
        return self.email

    def has_prem(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


