from cgi import print_exception
import email
from email.policy import default
from click import password_option
from django.db import models
from django.forms import CharField, UUIDField
from django.contrib.auth.models import User

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


#creating the courses table 
class Courses(models.Model):
    c_id = models.UUIDField()
    c_name = models.CharField(max_length=50)
    c_specification = models.CharField(max_length=100)
    c_specialty = models.CharField(max_length=100)
    publishing_time = models.DateTimeField()
    about_course = models.CharField(max_length=300)
    price = models.FloatField()
    c_link = models.CharField(max_length=300)
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.c_name, self.c_specification

    def Link(self):
        return self.c_link

    class Meta:
        ordering = ['c_name']

        