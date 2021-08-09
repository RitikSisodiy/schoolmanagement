from django.urls import path
from . import views
urlpatterns = [
    path('',views.student,name='student'),
    path('test/',views.test,name='test'),
    path('viewresult/',views.viewresult,name='viewresult'),
    path('viewattendance/',views.viewattendance,name='viewattendance'),
    path('profile/',views.myprofile,name='studentprofile'),
    path('studentleave/',views.studentleave,name='studentleave'),

]