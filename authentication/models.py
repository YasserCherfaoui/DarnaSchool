from cgi import print_exception
import email
from email.policy import default
from click import password_option
from django.db import models
from django.forms import CharField, UUIDField

# Create your models here.

#creating the student table 
class Students(models.Model):
    su_id = models.UUIDField()
    sname = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=50)
    profile_image = models.ImageField(default='default.png', blank=True)
    major = models.CharField(max_length=100)
    university_name = models.CharField(max_length=200)

    def Prf(self):
        return self.profile_image, self.sname

#creating the teacher table
class Teachers(models.Model):
    tu_id = models.UUIDField()
    tname = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=50)
    profile_image = models.ImageField(default='default.png', blank=True)
    level = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    about_teacher = models.CharField(max_length=300)
    
    def __str__(self):
        return self.tu_id

    def Prf(self):
        return self.profile_image, self.tname, self.level

