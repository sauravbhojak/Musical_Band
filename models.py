from pydoc import describe
from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    u_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=25)

class Admin(models.Model):
    Email       = models.EmailField(max_length=100)
    Password    = models.CharField(max_length=100)
    OTP         = models.IntegerField()
    is_created  = models.DateTimeField(auto_now_add=True)
    is_updated  = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    
class Artist(models.Model):
    user_id       = models.ForeignKey(Admin,on_delete=models.CASCADE)
    Firstname     = models.CharField(max_length=100)
    Role          = models.CharField(max_length=100)
    gender        = models.CharField(max_length=100)
    Contact       = models.CharField(max_length=100)     
    DOB           = models.CharField(max_length=100)
    profile_pic   = models.ImageField(upload_to="img/",default="abc.jpg")
    
class Team(models.Model):
    # user_id       = models.ForeignKey(Admin,on_delete=models.CASCADE)
    Name          = models.CharField(max_length=100)
    As_known_as   = models.CharField(max_length=100)
    Descricription = models.TextField(max_length=100) 
    Role          = models.CharField(max_length=100)
    Contact       = models.CharField(max_length=100)     
    DOB           = models.CharField(max_length=100)
    profile_pic   = models.ImageField(upload_to="img/",default="abc.jpg")
    
class event(models.Model):
    id    = models.AutoField(primary_key=True)
    Date  = models.CharField(max_length=100)
    Day   = models.CharField(max_length=50)
    Place = models.CharField(max_length=100)
    
class feedback_data(models.Model):
    Email = models.EmailField(max_length=50)
    Feedback = models.TextField(max_length=1000)
    created_at = models.DateTimeField(null=True,max_length=50)
    
class followers(models.Model):
    id = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(null=True,max_length=50)
    
    

class Book_show(models.Model):
    Email = models.EmailField(max_length=50)
    Details = models.TextField(max_length=1000)
    created_at = models.DateTimeField(null=True,max_length=50)
    
    
class Myvideos(models.Model):
    title=models.CharField(max_length=50)
    video =  models.FileField(upload_to="media/img/videos",null=True)
    
class Contact(models.Model):
    # user  = models.ForeignKey(User,on_delete=models.CASCADE)
    Name  = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Sub   = models.CharField(max_length=50)
    Msg   = models.TextField(max_length=500)
    created_at = models.DateTimeField(null=True,max_length=50)
    
class Highlight(models.Model):
    Follow  = models.ForeignKey(followers,on_delete=models.CASCADE)
    Show  = models.ForeignKey(Book_show,on_delete=models.CASCADE)
    Contact  = models.ForeignKey(Contact,on_delete=models.CASCADE)
    Feedback  = models.ForeignKey(feedback_data,on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True,max_length=50)
    
