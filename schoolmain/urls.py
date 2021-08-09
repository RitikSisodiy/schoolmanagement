from django.urls import path
from . import views
urlpatterns = [
    path('',views.schoolindex,name='schoolindex'),
    path('about/',views.about,name='schoolabout'),
    path('contact/',views.contact,name='schoolcontact'),
    path('admission/',views.admission,name='schooladmission'),
    path('admission/highschoo/',views.highschool,name='highschooladmission'),
]