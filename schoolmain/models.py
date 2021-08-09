from django.db import models

# Create your models here.
class schoolifo(models.Model):
    icon = models.ImageField(upload_to = 'schoolinfo')
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
class schoocontact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    lookingfor = models.CharField(max_length=25)
    massage = models.CharField(max_length=25)
