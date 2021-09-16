from django.urls import path
from . import views
urlpatterns = [
    path('',views.schoolindex,name='schoolindex'),
    path('about/',views.about,name='schoolabout'),
    path('contact/',views.contact,name='schoolcontact'),
    path('admission/',views.admission,name='schooladmission'),
    path('admission/<slug:feeslug>/',views.admissionfee,name='admissionfee'),
    path('admission/highschool/',views.highschool,name='highschooladmission'),
    path('admission/kiddergarden/',views.kiddergarden,name='kiddergardenadmission'),
    path('admission/smallschool/', views.smallschool, name='smallschooladmission'),
    path('admission/middleschool/', views.middleschool, name='middleschooladmission'),
    path('learnings',views.learnings,name='learnings'),
]