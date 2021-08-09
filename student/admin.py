from django.contrib import admin
from .models import studentregister,standard,subject,Class,gender
# Register your models here.
admin.site.register(studentregister)
admin.site.register(standard)
admin.site.register(subject)
admin.site.register(gender)
@admin.register(Class)
class ClassModelAdmin(admin.ModelAdmin):
    list_display = ['standard','subject']