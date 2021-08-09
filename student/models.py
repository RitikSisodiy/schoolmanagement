from django.db import models
from django.contrib.auth.models import User
# Create your models hec
class subject(models.Model):
    subject = models.CharField(max_length=50)
    def __str__(self):
        return self.subject
class standard(models.Model):
    standard = models.CharField(max_length=30)
    def __str__(self):
        return self.standard
class Class(models.Model):
    subject= models.ForeignKey(subject,on_delete=models.CASCADE)
    standard= models.ForeignKey(standard,on_delete=models.CASCADE)
    def __str__(self):
        return self.subject.subject
class gender(models.Model):
    gender = models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.gender
class studentregister(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)    
    Father_name = models.CharField(max_length = 25)
    Mother_name = models.CharField(max_length = 25)
    schooler_no = models.CharField(max_length = 25)
    gender = models.ForeignKey(gender,on_delete=models.CASCADE)
    dob = models.DateField()
    cast = models.CharField(max_length=20)
    addmission_date  =models.DateField()
    standard = models.ForeignKey(standard,on_delete=models.CASCADE)
    ssmid  =models.CharField(max_length=20)
    addhar_no  =models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    account_no = models.CharField(max_length=20) 
    IFSC = models.CharField(max_length=20) 
    TC = models.FileField(upload_to="certificate",blank=True) 
    castcertificate = models.FileField(upload_to='certificate',blank=True)
    status = models.BooleanField(default=False)
    phonestatus = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.email)
class leavestudent(models.Model):
    student_id = models.ForeignKey(studentregister(), on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)