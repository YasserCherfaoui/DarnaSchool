from cgi import print_exception
import email
from email.policy import default
from click import password_option
from django.db import models
from django.forms import CharField, UUIDField
from authentication.models import Teachers, Students

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


#creating the courses comments table
class C_comment(models.Model):
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    c_id = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.BinaryField()
    comment_time = models.DateTimeField()


