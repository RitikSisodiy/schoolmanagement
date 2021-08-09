from django.db import models
from django.contrib.auth.models import User
class otp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=10)