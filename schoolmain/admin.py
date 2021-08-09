from django.contrib import admin
from .  models import schoolifo
# Register your models here.
@admin.register(schoolifo)
class schoolinfoAdmin(admin.ModelAdmin):
    list_display = ['email','phone']