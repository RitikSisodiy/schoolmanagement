from django.contrib import admin
from .models import staffregister,examtype,result,studentAttendance
# Register your models here.
admin.site.register(staffregister)
admin.site.register(examtype)
admin.site.register(result)
admin.site.register(studentAttendance)