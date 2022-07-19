from cgi import print_exception
import email
from email.policy import default
from click import password_option
from django.db import models
from django.forms import CharField, UUIDField
from authentication.models import Teachers, Students
from darnaSchool.m_courses import Courses


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
        
   
#creating the wallet table
class C_comment(models.Model):
    tu_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True, blank=True)
    su_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    amo_bfor = models.FloatField()
    amo_after = models.FloatField()
    change_or_buy = models.IntegerField()
    time = models.DateTimeField()
    p_method = models.ForeignKey(P_method, on_delete=models.CASCADE, null=True, blank=True)

