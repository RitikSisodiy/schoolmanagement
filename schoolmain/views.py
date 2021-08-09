from django.shortcuts import render
from .models import  schoolifo,schoocontact
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myapp.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.
def schoolindex(request):
    return render(request,'schoolmain/index.html',{})
def about(request):
    return render(request,'schoolmain/about.html',{})
def contact(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        lookingfor = request.POST['lookingfor']
        massage = request.POST['massage']
        contactob = schoocontact(name=name,email=email,address=address,lookingfor=lookingfor,massage=massage)
        contactob.save()
        subject = "Contact mail from school"
        maildic = {
            'name':name,
            'email':email,
            'address':address,
            'lookingfor':lookingfor,
            'massage':massage
        }
        html_message = render_to_string('schoolmain/contactmail.html',maildic)
        plain_message = strip_tags(html_message)
        from_email = EMAIL_HOST_USER
        to = 'ritik.s10120@gmail.com'
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    info = schoolifo.objects.all()[0]
    return render(request,'schoolmain/contact.html',{'info':info})
def admission(request):
    return render(request,'schoolmain/admission.html',{})
def highschool(request):
    return render(request,'schoolmain/highschool.html',{})