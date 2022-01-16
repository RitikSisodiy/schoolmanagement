from django.shortcuts import render, get_object_or_404
from .models import  Gallery, schoolifo,contactform,schoolfeeinfo,aboutlearning,admissionform,recentprogram,activity
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myapp.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . models import kidsinfo
from django.contrib import messages
# Create your views here.
def schoolindex(request):
    if request.method == "POST":
        kname = request.POST['kname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        studying =  request.POST['studying']
        requirement = request.POST['requirement']
        study_collection = [1,2,3]
        if len(kname)<1 or len(email)<3 or len(phone_number)<10 or len(requirement)<4:
            messages.error(request,"please fill the form correctly")
        else:
            askkidinfo =kidsinfo(kname=kname,email =email,phone_number =phone_number,studying=studying,requirement=requirement)
            askkidinfo.save()
            messages.success(request,"Your form has been submitted successfull")
    return render(request,'schoolmain/index.html',{})
def about(request):
    if request.method == "POST":
        kname = request.POST['kname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        studying =  request.POST['studying']
        requirement = request.POST['requirement']
        study_collection = [1,2,3]
        if len(kname)<1 or len(email)<3 or len(phone_number)<10 or len(requirement)<4:
            messages.error(request,"please fill the form correctly")
        else:
            askkidinfo =kidsinfo(kname=kname,email =email,phone_number =phone_number,studying=studying,requirement=requirement)
            askkidinfo.save()
            messages.success(request,"Your form has been submitted successfull")
    return render(request,'schoolmain/about.html',{})
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        looking_for = request.POST['looking_for']
        massage = request.POST['massage']
        if len(name)<3 or len(email)<3 or len(massage)<5:
            messages.error(request,"Try again")
        else:
            messages.success(request,"Your form is submitted  successfull")
            contactob = contactform(name=name,email=email,address=address,looking_for=looking_for,massage=massage)
            contactob.save()

        # subject = "Contact mail from school"
    #     maildic = {
    #         'name':name,
    #         'email':email,
    #         'address':address,
    #         'looking_for':looking_for,
    #         'massage':massage
    #     }
    #     html_message = render_to_string('schoolmain/contactmail.html',maildic)
    #     plain_message = strip_tags(html_message)
    #     from_email = EMAIL_HOST_USER
    #     to = 'ritik.s10120@gmail.com'
    #     send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    info = schoolifo.objects.all()[0]

    return render(request,'schoolmain/contact.html',{'info':info})
def admission(request):
    fee = schoolfeeinfo.objects.all()
    if request.method == "POST":
        kname = request.POST['kname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        studying =  request.POST['studying']
        requirement = request.POST['requirement']
        study_collection = [1,2,3]
        if len(kname)<1 or len(email)<3 or len(phone_number)<10 or len(requirement)<4:
            messages.error(request,"please fill the form correctly")
        else:
            askkidinfo =kidsinfo(kname=kname,email =email,phone_number =phone_number,studying=studying,requirement=requirement)
            askkidinfo.save()
            messages.success(request,"Your form has been submitted successfull")
    return render(request,'schoolmain/admission.html',{'stdadmission':fee})
def admissionfee(request, feeslug=""):
    feedata = get_object_or_404(schoolfeeinfo,slug=feeslug)
    fee = schoolfeeinfo.objects.all()
    program = recentprogram.objects.all()
    active = activity.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email=request.POST['email']
        contact_no=request.POST['contact_no']
        messages= request.POST['messages']
        admission = admissionform(name= name,email=email,contact_no=contact_no,messages=messages)
        admission.save()
        #     messages.success(request, "Your form is submiited")
        #     messages.error(request,"Form is not submitted")
    return render(request,'schoolmain/school-fees-details.html',{'stdadmission':fee, 'feedata': feedata, 'currentfee':feeslug,'program':program,'active':active})
def kiddergarden(request):
    return render(request,'schoolmain/school-fees-details.html',{})
def smallschool(request):
    return render(request,'schoolmain/smallschool.html',{})
def middleschool(request):
    return render(request,'schoolmain/middleschool.html',{})
def highschool(request):
    return render(request,'schoolmain/highschool.html',{})
def learnings(request):
    standardinfo = aboutlearning.objects.all()
    if request.method == "POST":
        kname = request.POST['kname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        studying =  request.POST['studying']
        requirement = request.POST['requirement']
        study_collection = [1,2,3]
        if len(kname)<1 or len(email)<3 or len(phone_number)<10 or len(requirement)<4:
            messages.error(request,"please fill the form correctly")
        else:
            askkidinfo =kidsinfo(kname=kname,email =email,phone_number =phone_number,studying=studying,requirement=requirement)
            askkidinfo.save()
            messages.success(request,"Your form has been submitted successfull")
    return render(request,'schoolmain/learnings.html',{'details':standardinfo})
def gallery(request):
    res={}
    res['gallerys'] = Gallery.objects.all()
    return render(request,'schoolmain/gallery.html',res)