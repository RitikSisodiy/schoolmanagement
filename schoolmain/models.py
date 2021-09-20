from django.db import models
from ckeditor.fields import RichTextField
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

class kidsinfo(models.Model):
    kname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    studying = models.CharField(max_length=500)
    requirement = models.CharField(max_length=150)

class schoolfeeinfo(models.Model):
    standards = models.CharField(max_length=100,blank=False)
    slug = models.CharField(max_length=100,null=False,unique=True)
    annualfee = models.IntegerField()
    yearlysormonthly = models.CharField(max_length=150)
    content = RichTextField()
    cen_img = models.FileField(upload_to="img")
    cen_content = models.CharField(max_length=250)
    title1 = models.CharField(max_length=50)
    content1 = models.CharField(max_length=1000)
    content11 = RichTextField()
    title2 = models.CharField(max_length=50)
    content2 = models.CharField(max_length=1000)
    content22 = models.CharField(max_length=1000)
    image2 = models.FileField(upload_to="img")
    title3= models.CharField(max_length=50)
    content3 = models.CharField(max_length=1000)
    content33 = models.CharField(max_length=1000)
    image3 = models.FileField(upload_to="img")
    title4 = models.CharField(max_length=50)
    content4 = models.CharField(max_length=1000)
    content44 = models.CharField(max_length=1000)
    image4 = models.FileField(upload_to="img")


class contactform(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    looking_for = models.CharField(max_length=50)
    massage = models.TextField(max_length=500)

class aboutlearning(models.Model):
    standard = models.CharField(max_length=200)
    classes = models.CharField(max_length=100)
    information = models.CharField(max_length=1000)
    content = RichTextField()

class admissionform(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact_no = models.IntegerField()
    messages = models.CharField(max_length=500)

class recentprogram(models.Model):
    date = models.CharField(max_length=31)
    month = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    time = models.DurationField()
    heading_title = models.CharField(max_length=100)

class activity(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    img = models.FileField(upload_to="img")



