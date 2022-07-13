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


#creating the payment pethod table
class P_method(models.Model):
    P_id = models.UUIDField()
    p_name = models.CharField(max_length=50)

#creating the transactions table 
class Transactions(models.Model):
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    c_id = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    p_method = models.ForeignKey(P_method, on_delete=models.CASCADE, null=True, blank=True)
    transaction_time = models.DateTimeField()
    price = models.FloatField()
    f_price = models.FloatField()
    

    def __str__(self):
        return self.su_id, self.c_id, self.transaction_time 

    class Meta:
        ordering = ['transaction_time']
        
#creating the courses comments table
class C_comment(models.Model):
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    c_id = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.BinaryField()
    comment_time = models.DateTimeField()

#creating the wallet table
class C_comment(models.Model):
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    amo_bfor = models.FloatField()
    amo_after = models.FloatField()
    change_or_buy = models.IntegerField()
    time = models.DateTimeField()
    p_method = models.ForeignKey(P_method, on_delete=models.CASCADE, null=True, blank=True)

#creating the post table
class Post(models.Model):
    p_id = models.UUIDField()
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    post = models.BinaryField()

#creating the replay post
class Replay(models.Model):
    p_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    replay = models.BinaryField()

