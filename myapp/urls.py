"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schoolmain.urls')),
    path('', views.index, name = 'index'),
    path('studentregister/', views.register, name = 'studentregister'),
    path('staffregister/', views.register, name = 'staffregister'),
    path('dashboard/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
    path('verifymail/', views.verifymail, name = 'verify'),
    path('staff/' , include('staff.urls')),
    path('student/' , include('student.urls')),
    path('sendmail/' , views.sendmail),
    path('verifyphone/' , views.verifyotp),
    path('result/' , views.results,name='getresult'),
    path('students/' , views.students,name="getstudents"),
    path('updatenav/' , views.updatenav,name="updatenav"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
