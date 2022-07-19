from cgi import print_exception
import email
from email.policy import default
from click import password_option
from django.db import models
from django.forms import CharField, UUIDField
from authentication.models import Teachers, Students

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
