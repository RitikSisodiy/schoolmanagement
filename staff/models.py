from django.db import models
from django.contrib.auth.models import User
from student.models import standard,subject,Class,studentregister
# Create your models hec
class staffregister(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    subject  = models.CharField(max_length = 10)
    phone  = models.CharField(max_length = 30 )
    address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    phonestatus = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.first_name+" "+self.user.last_name+" ( "+self.user.email+" )")
class classtimings(models.Model):
    user = models.ForeignKey(staffregister,on_delete=models.CASCADE)
    Class = models.ForeignKey(standard,on_delete=models.CASCADE)
    subject = models.ForeignKey(subject,on_delete=models.CASCADE)
    timefrom = models.TimeField()
    timeto  = models.TimeField()
    def __str__(self):
        return str(self.user.user.email)
class examtype(models.Model):
    Class = models.ForeignKey(standard,on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
class result(models.Model):
    exam = models.ForeignKey(examtype,on_delete=models.CASCADE)
    student = models.ForeignKey(studentregister,on_delete=models.CASCADE)
    subject = models.ForeignKey(subject,on_delete=models.CASCADE)
    obtain_marks = models.CharField(max_length=5)
    max_marks = models.CharField(max_length=5)
class studentAttendance(models.Model):
    standard = models.ForeignKey(standard, on_delete=models.CASCADE)
    student = models.ForeignKey(studentregister,on_delete=models.CASCADE)
    date = models.DateField()
    attend = models.BooleanField(default=False)
