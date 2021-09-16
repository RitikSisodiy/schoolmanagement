from django.contrib import admin
from .  models import schoolifo,kidsinfo,schoolfeeinfo,contactform,aboutlearning,feedetails,admissionform,recentprogram,activity
# Register your models here.
admin.site.register(kidsinfo)
admin.site.register(schoolfeeinfo)
admin.site.register(contactform)
admin.site.register(aboutlearning)
admin.site.register(feedetails)
admin.site.register(admissionform)
admin.site.register(recentprogram)
admin.site.register(activity)



@admin.register(schoolifo)
class schoolinfoAdmin(admin.ModelAdmin):
    list_display = ['email','phone']