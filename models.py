from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver as re
from django.utils.text import slugify

from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a Username')
        
        print('creating user')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):

        
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_staff=True
        user.is_active=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)

        
        return user


class User(AbstractBaseUser):
    username                    = models.CharField(max_length=63, blank=True, null=True, unique=True, verbose_name="Username")
    email                       = models.EmailField(max_length=225, blank=True, null=False, verbose_name="Email Field")
    is_staff                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)     
    is_admin                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)
    date_joined                 = models.DateTimeField(auto_now_add=True)   
    last_login                  = models.DateTimeField(auto_now=True)
    profile_pic                 = models.ImageField(null=True, blank=True)


    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username


class App(models.Model):
    id              = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    url             = models.CharField(max_length=225,blank=True,null=True)
    as_app_select   = models.BooleanField(default=False)
    sequence        = models.IntegerField(blank=True, null=True)
    icon_class      = models.CharField(max_length=225, blank=True, null=True)
    user_list       = models.CharField(max_length=225, blank=True, null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="app_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="app_updated_by")

    def __str__(self):
        return self.name
    

class Page(models.Model):
    id                  = models.IntegerField(primary_key=True)
    app                 = models.ForeignKey(App,null=True,blank=True,on_delete=models.SET_NULL)
    name                = models.CharField(max_length=225,unique=True)
    description         = models.CharField(max_length=225,blank=True,null=True)
    path                = models.CharField(max_length=225,unique=True,blank=True,null=True)
    is_enabled          = models.BooleanField(default=False)
    is_action_button    = models.BooleanField(default=False)
    created_date        = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date        = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by          = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="page_created_by")
    updated_by          = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="page_updated_by")

    def __str__(self):
        return self.name
        

class Group(models.Model):
    id              = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="group_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="group_updated_by")

    def __str__(self):
        return self.name


class GroupApp(models.Model):
    group=models.ForeignKey(Group, null=True,on_delete=models.SET_NULL)  
    app=models.ForeignKey(App,null=True,on_delete=models.SET_NULL)


class GroupPage(models.Model):
    group=models.ForeignKey(Group,null=True,on_delete=models.SET_NULL)  
    page=models.ForeignKey(Page,null=True,on_delete=models.SET_NULL)    


class UserGroup(models.Model):
    id              = models.IntegerField(primary_key=True)
    user            = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    group           = models.ForeignKey(Group,null=True,on_delete=models.SET_NULL)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="user_group_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="user_group_updated_by")

    def __str__(self):
        return f"{self.user.id} - {self.group.name}"  
    
    
class Role(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="role_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="role_updated_by")


class ContactType(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="contact_type_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="contact_type_updated_by")

    def __str__(self):
        return self.name
    

class AddressType(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="address_type_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="address_type_updated_by")

    def __str__(self):
        return self.name
    

class FamilyRelationshipType(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="family_relationship_type_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="family_relationship_type_updated_by")

    def __str__(self):
        return self.name      
    

class Gender(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="gender_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="gender_updated_by")

    def __str__(self):
        return self.name    
    

class BloodType(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="blood_type_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="blood_type_updated_by")

    def __str__(self):
        return self.name     
    

class Suffix(models.Model):
    name            = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    is_enabled      = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="suffix_created_by")
    updated_by      = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="suffix_updated_by")

    def __str__(self):
        return self.name        
    

class Citizenship(models.Model):
    name                = models.CharField(max_length=225,unique=True)
    iso_country_code    = models.CharField(max_length=225,blank=True,null=True)
    description         = models.CharField(max_length=225,blank=True,null=True)
    is_enabled          = models.BooleanField(default=False)
    created_date        = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date        = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by          = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="citizenship_created_by")
    updated_by          = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="citizenship_updated_by")

    def __str__(self):
        return self.name      
    

class ActivityType(models.Model):
    name                = models.CharField(max_length=225,unique=True)
    description         = models.CharField(max_length=225,blank=True,null=True)
    is_enabled          = models.BooleanField(default=False)
    created_date        = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date        = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by          = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="activity_type_created_by")
    updated_by          = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE, related_name="activity_type_updated_by")

    def __str__(self):
        return self.name      


class ActivityLog(models.Model):
    app=models.ForeignKey(App,null=True,blank=True,on_delete=models.SET_NULL)
    page=models.ForeignKey(Page,null=True,blank=True,on_delete=models.SET_NULL)
    remarks=models.TextField()
    created_by=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="activity_log_created_by")
    created_date=models.DateTimeField(default=datetime.now,blank=False)


# class Notification(models.Model):
#     page=models.ForeignKey(Page,null=True,blank=True,on_delete=models.SET_NULL)
#     remarks=models.TextField()
#     is_read=models.BooleanField(default=False)
#     created_by=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="notification_created_by")
#     recipient=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="recipient_created_by")
#     created_date=models.DateTimeField(default=datetime.now,blank=False)


# @re(post_save,sender=User)
# def post_create_user(instance,created,**kwargs):
#     if created:
#         AppUser.objects.create(app=App.objects.get(id=100),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=100001),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=100002),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=100003),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=100004),user=instance)

#         AppUser.objects.create(app=App.objects.get(id=101),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=101001),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=101002),user=instance)
#         PageUser.objects.create(page=Page.objects.get(id=101003),user=instance)