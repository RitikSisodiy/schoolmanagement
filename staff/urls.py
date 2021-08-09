from django.urls import path 
from django.conf.urls import url
from . import views
from django.views.i18n import JavaScriptCatalog
urlpatterns= [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('',views.staff,name='staff'),
    path('result/',views.studentresult,name='result'),
    path('result/delete/',views.deleteresult,name='deleteresult'),
    path('result/<slug:std>/',views.studentresult,name='result'),
    path('info/<slug:std>/',views.studentinfo,name='studentinfo'),
    path('result/<slug:std>/view/',views.viewresult,name='result'),
    path('schedule/',views.allschedule,name='allschedule'),
    path('mystudent/',views.mystudent,name='mystudent'),
    path('mystudent/<slug:std>/',views.mystudent,name='mystudent'),
    path('classes/subjects/',views.subjects,name='subjects'),
    path('classes/',views.classes,name='classes'),
    path('staff/',views.users,name='managestaff'),
    path('manageattendance/',views.manageattendance,name='manageattendance'),
    path('managestudentleave/',views.managestudentleave,name='managestudentleave'),
    path('profile/',views.myprofile,name='staffprofile'),
    path('schoolinfo/',views.schoolinfo,name='schoolinfo'),
]