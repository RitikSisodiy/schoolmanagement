from django.shortcuts import render,redirect
from .forms import StaffRegister,userRegister,loginform
from .forms import StaffRegister,userRegister,loginform,StudentRegister
from django.http import HttpResponse
from staff.models import staffregister,result,examtype
from student.models import studentregister
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from .verify import send_token,verify_token
import string
import random
from .models import otp
from .forms import otpform
from .sendsms import sendotp
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
  
def index(request):
    stuid = request.GET.get('stuid')
    examsob = []
    if stuid is not None:
        examlist = result.objects.values('exam')
        exams={item['exam'] for item in examlist}
        for exam in exams:
            resultlist = result.objects.filter(student=stuid,exam=exam)
            if resultlist.exists():
                examob = examtype.objects.get(id=exam)
                examsob.append(examob)
        return render(request,'index.html',{'exams':examsob,'stuid':stuid})
    return render(request,'index.html',{})
def students(request):
    stulist = studentregister.objects.all()
    return render(request,'index.html',{'stulist':stulist})
def checkuser(request):
    user= None
    userob= None
    if staffregister.objects.filter(user = request.user.id).exists():
        userob = staffregister.objects.filter(user = request.user.id)[0]
        user = 'staff' 
    if studentregister.objects.filter(user = request.user.id).exists():
        userob = studentregister.objects.filter(user = request.user.id)[0]
        user = 'student'
    if user is None and userob is None:
        logout(request)
        return redirect('index')
    return [user,userob]
def results(request):
    examid = request.GET.get('exam')
    stuid = request.GET.get('stuid')
    getpdf = request.GET.get('getpdf')
    resultobj = result.objects.filter(student=stuid,exam=examid)
    if resultobj.exists():
        from django.db.models import Sum
        from .resultopration import per
        total = resultobj.aggregate(Sum('obtain_marks'),Sum('max_marks'))
        res = per(list(total.values())[0],list(total.values())[1],resultobj)
        if getpdf == 'print':
            result_pdf = renderPdf('pdfresult.html',{'mainresult':resultobj,'total':res},request)
            return HttpResponse(result_pdf,content_type='application/pdf')
        return render(request,'result.html',{'mainresult':resultobj,'total':res})
    return redirect('index')
def register(request):
    name = "student" if str(request.path).find('studentregister') != -1 else "staff"
    print(name)
    if request.user.is_authenticated:
        return redirect(checkuser(request)[0])
    if request.method =='POST':
        form = userRegister(request.POST)
        if name == 'staff':
            form1 = StaffRegister(request.POST,request.FILES)
        else:
            form1 = StudentRegister(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid() and form1.is_valid(): 
            username = res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 10))
            password = form.cleaned_data['password']
            obj = form.save(commit=False)
            obj.username = username
            obj.save()
            user = User.objects.get(username=username)
            user.password = make_password(password)
            user.save()
            obj = form1.save(commit=False)
            obj.user = user
            obj.save()
            send_token(request,form.cleaned_data['email'],name)
            return redirect(name+'register')
        else:
            messages.error(request,"please check your form")
            return render(request ,'register.html',{'form':[form,form1]})
    form = [userRegister(),StaffRegister()] if name == 'staff' else [userRegister(),StudentRegister()]
    res = {
        'form':form,
        'name':name,
    }
    return render(request ,'register.html',res)
def signin(request):
    if request.user.is_authenticated:
        return redirect('staffregister')
    if request.method=='POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = User.objects.get(email=form.cleaned_data['username']).username
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully')
                return redirect(request.path)
            else:
                messages.error(request,"please check your password")
                return render(request,'signin.html',{'form':form})
        else:
            return render(request,'signin.html',{'form':form})

    form = loginform()
    return render(request,'signin.html',{'form':form})
def signout(request):
    logout(request)
    messages.success(request,"Log out successfully")
    return redirect('index')
def verifymail(request):
    username = request.GET['user']
    verify = request.GET['verify']
    token = request.GET['token']
    token = token.replace(' ','+')
    verify = verify.replace(' ','+')
    if verify_token(verify,username,token):
        user = User.objects.get(email=username)
        print(user.id)
        if staffregister.objects.filter(user = user.id).exists():
            user = staffregister.objects.filter(user = user.id)[0]
        if studentregister.objects.filter(user = user.id).exists():
            user = studentregister.objects.filter(user = user.id)[0]
        user.status = True
        user.save()
        return HttpResponse('email is successfully verfied')
    else:
        return HttpResponse("<h2>404 invalid request or verifiction link is expired</h2>")
def sendmail(request):
    if request.user.is_authenticated:
        useras = checkuser(request)
        if useras[0] is not None:
            send_token(request,request.user.email,useras[0])
            messages.success(request,"email is sent successfully")
            return redirect(useras[0])
        return redirect('register')
def verifyotp(request):
    useras = checkuser(request)
    to = useras[0]
    user = useras[1]
    if user.phonestatus == False:
        if request.method=='POST':
            if to is not None:
                form = otpform(request.POST)
                if form.is_valid():
                    OTP = form.cleaned_data['otp']
                    obj = otp.objects.filter(user=request.user,otp=OTP)
                    if obj.exists():
                        obj = None
                        if to == 'staff':
                            obj = staffregister.objects.filter(user=request.user)[0]
                        if to == 'student':
                            obj = studentregister.objects.filter(user=request.user)[0]
                        if obj is not None:
                            obj.phonestatus = True
                            obj.save()
                            return redirect('register')
                    else:
                        return HttpResponse("not exicst")
                else:
                    return render(request,'verifyotp.html',{"form":form})
        if request.user.is_authenticated and to is not None:
            a = ''
            for i in range(6):
                a=a+str(random.randint(0,9))
            if otp.objects.filter(user=request.user).exists():
                otp.objects.get(user=request.user).delete()
            otp(user=request.user,otp =a).save()
            status = sendotp(user.phone,a)
            if status is False or status is None:
                return HttpResponse("there is some error in sending otp please try afer some time")
            return render(request,'verifyotp.html',{"form":otpform(),'for':to})                
def renderPdf(template, content,request):
    t = get_template(template)
    send_data = t.render(content,request)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(send_data.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return None
def updatenav(request):
    request.session['nav'] = request.GET.get('nav')
    print(request.session['nav'])
    print(request.GET.get('nav'))
    return HttpResponse("done")