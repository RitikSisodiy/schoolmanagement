from django.shortcuts import render,redirect
from django.http import HttpResponse
# from render_block.base import render_block_to_string
from .models import staffregister,Class,standard,result
from student.models import studentregister,subject,leavestudent
from django.core import serializers
from myapp.forms import StaffRegister,userRegister,StudentRegister
import random
import string
from schoolmain.models import schoolifo
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json
from threading import Thread
from django.contrib import messages
from .forms import ClassForm,subjectForm,classtimingsForm,classtimings,examtypeForm,examtype,standardForm,updatestudentUserForm,schoolinfoForm
from . models import studentAttendance
# Create your views here.
def staff(request):
    res = {}
    data = serializers.serialize( "python",staffregister.objects.filter(user=request.user.id))
    res['data'] = data
    res['noofstudent'] = studentregister.objects.all().count()
    res['noofstaff'] = staffregister.objects.all().count()
    res['noofclass'] = standard.objects.all().count()
    res['noofsubject'] = subject.objects.all().count()
    subnamelist = []
    subcountlist = []
    studentcountlist = []
    for sub in standard.objects.all():
        count = Class.objects.filter(standard=sub.id).count()
        stucount = studentregister.objects.filter(standard=sub.id).count()
        name = sub.standard
        subnamelist.append(name)
        subcountlist.append(count)
        studentcountlist.append(stucount)
    res['subnamelist'] = subnamelist
    res['subcountlist'] = subcountlist
    res['studentcountlist'] = studentcountlist
    if request.user.staffregister_set.all()[0].status == False:
        res['verify'] = 'notverifyed'
    return render(request,'staff/dashboard.html',res)
def studentinfo(request,std=None):
    if request.GET.get('id') is not None:
        # stu = serializers.serialize('python',studentregister.objects.filter(id=request.GET['id']))
        # stuuser = studentregister.objects.get(id=request.GET.get('id'))
        # return render(request,'staff/studentinfo.html',{'studentinfo':stu,'stuuser':stuuser})
        user = studentregister.objects.get(id=request.GET['id'])
        form1 = updatestudentUserForm(instance=user.user)
        form= StudentRegister(instance=user)
        if request.method == "POST":
            form = StudentRegister(request.POST,request.FILES,instance=user)
            form1 = updatestudentUserForm(request.POST,request.FILES,instance=user.user)
            if form.is_valid() and form1.is_valid():
                form.save()
                form1.save()
            messages.success(request, "student is updated succesfully")
            return redirect(request.get_full_path())
        return render(request,'staff/studentinfo.html',{'studentuser':user,'form':form,'form1':form1})



        
    studentlist = studentregister.objects.all().order_by('user__first_name')
    res = {
        'student':studentlist
    }
    return render(request,'staff/studentinfo.html',res)
def delstudent(request,username=None):
    if username is not None:
        try:
            userob = User.objects.get(username=username)
            messages.success(request,f"{userob.first_name} {userob.last_name} is deleted successfully")
            userob.delete()
        except:
            messages.error(request,"invalid request")
    else:
        messages.error(request,"invalid request")
    return redirect('mystudentall')
def studentresult(request,std):
    std = standard.objects.get(standard=std)
    stuid = request.GET.get('stuid')
    if request.method == 'POST':
        form = examtypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Result is updated successfully")
            return redirect(request.get_full_path())
        else:
            messages.error(request,"invalid data please check the deatails")
    form = examtypeForm(initial={'Class': std.id})
    exam = examtype.objects.filter(Class=std.id)
    res = {
        'form':form,
        'exams':exam,
        'stuid':stuid
        }
    return render(request,'staff/result.html',res)
def schedule(request):
    user = staffregister.objects.get(user=request.user.id)
    schedule = classtimings.objects.filter(user=user.id)
    if request.method == 'POST':
        form = classtimingsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user
            checksub = classtimings.objects.filter(Class=obj.Class,subject=obj.subject)
            if checksub.exists():
                return render(request,'staff/schedule.html',{'forms':form,'schedule':schedule,"message":"this subject class is taken by staff member "+str(checksub[0].user.user.first_name)+" "+str(checksub[0].user.user.last_name +" at "+ str(checksub[0].timefrom))})
            checktiming = classtimings.objects.filter(Class=obj.Class,timefrom=obj.timefrom)
            if checktiming.exists():
                return render(request,'staff/schedule.html',{'forms':form,'schedule':schedule,"message":"this timing is busy with staff member "+str(checktiming[0].user.user.first_name)+" "+str(checktiming[0].user.user.last_name)})
            obj.save()
    else:
        form = classtimingsForm()
    delschedule = request.GET.get('schedule')
    if delschedule is not None:
        try:
            classtimings.objects.get(id=delschedule).delete()
            return redirect('schedule')
        except:
            pass
    res = {
        'forms':form,
        'schedule':schedule,
    }
    return render(request,'staff/schedule.html',res)
def allschedule(request):
    if request.user.is_superuser:
        user = staffregister.objects.get(user=request.user.id)
        schedule = classtimings.objects.filter(user=user.id)
        classes = standard.objects.all()
        if request.method == 'POST':
            form = classtimingsForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                checksub = classtimings.objects.filter(Class=obj.Class,subject=obj.subject)
                if checksub.exists():
                    messages.error(request,"this subject class is taken by staff member "+str(checksub[0].user.user.first_name)+" "+str(checksub[0].user.user.last_name +" at "+ str(checksub[0].timefrom)))
                    return redirect(request.get_full_path())
                checktiming = classtimings.objects.filter(Class=obj.Class,timefrom=obj.timefrom)
                if checktiming.exists():
                    messages.error(request,"this timing is busy with staff member "+str(checktiming[0].user.user.first_name)+" "+str(checktiming[0].user.user.last_name))
                    return redirect(request.get_full_path())
                checktiming = classtimings.objects.filter(user=obj.user,timefrom=obj.timefrom)
                if checktiming.exists():
                    messages.error(request,str(checktiming[0].user.user.first_name)+" "+str(checktiming[0].user.user.last_name)+ " has ( " + str(checktiming[0].subject.subject) +" ) preiod in "+ str(checktiming[0].Class.standard) +" class in this time slot ! Please choose the different timing   ")
                    return redirect(request.get_full_path())
                obj.save()
                messages.success(request,"New schedule is added successfully.....")
                return redirect(request.get_full_path())
        else:
            form = classtimingsForm()
        delschedule = request.GET.get('schedule')
        classid = request.GET.get('id')
        if delschedule is not None:
            try:
                classtimings.objects.get(id=delschedule).delete()
                messages.success(request,"schedule is deleted successfully....")
                return redirect(str(request.path)+"?id="+classid)
            except:
                pass
        if classid is not None:
            sublist = Class.objects.filter(standard = classid)
            schedulelist = []
            for sub in sublist:
                sch = classtimings.objects.filter(Class=classid,subject=sub.subject.id)
                schedulelist.append([sub,sch])
            form = classtimingsForm(initial={'Class': classid,})           
            return render(request,'staff/allschedule.html',{'schedulelist':schedulelist,'forms':form})
        
        res = {
            'forms':form,
            'schedule':schedule,
            
        }
        subnamelist = []
        subcountlist = []
        studentcountlist = []
        emptyperiod = []
        for sub in classes:
            count = Class.objects.filter(standard=sub.id).count()
            stucount = studentregister.objects.filter(standard=sub.id).count()
            emptyper = Class.objects.filter(standard=sub.id).count() - classtimings.objects.filter(Class=sub.id).count()
            subcountlist.append(count)
            studentcountlist.append(stucount)
            emptyperiod.append(emptyper)
        res['classSubStulist'] = zip(classes,subcountlist,studentcountlist,emptyperiod)
        return render(request,'staff/allschedule.html',res)
    return redirect('staff')
def mystudent(request,std=None):
    staffuser = staffregister.objects.get(user=request.user.id)   
    if std is not None:
        stuclass = standard.objects.get(standard=std)
        mystudent = studentregister.objects.filter(standard=stuclass.id)
        res = {
            'mystudent':mystudent
        }
    else:
        myclasses = standard.objects.all()
        # myclasses = classtimings.objects.filter(user= staffuser.id)
        res= {
            'myclass':myclasses
        }
    return render(request,'staff/mystudent.html',res)
def mystudentall(request):
    stulist = studentregister.objects.all()
    res = {'stulist':stulist}
    res['form'] = userRegister()
    res['form1'] = StudentRegister()
    if request.method == "POST":
        res['form'] = userRegister(request.POST)
        res['form1'] = StudentRegister(request.POST,request.FILES)
        if res['form'].is_valid() and res['form1'].is_valid():
            form = res['form']
            form1 = res['form1']
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
            messages.success(request,str(form.instance.first_name)+ " "+str(form.instance.first_name) +" is Added Successfully")
            return redirect(request.get_full_path())
        else:
            messages.error(request,'Invalid student data !')
    return render(request,'staff/mystudentall.html',res)
from myapp.views import sendresult
def viewresult(request,std=None):
    examid = request.GET.get('exam')
    std = standard.objects.get(standard=std)
    stuid = request.GET.get('stuid')
    if request.method == 'POST':
        examobj = examtype.objects.get(id=examid)
        sublist = Class.objects.filter(standard=std.id)
        for sub in sublist:
            # print(request.POST.get(str(sub.subject)),request.POST.get('max-'+str(sub.subject)),sub.subject)
            obmarks = request.POST.get(str(sub.subject)) if request.POST.get(str(sub.subject)) is not '' else '0'
            mxmarks = request.POST.get('max-'+str(sub.subject)) if request.POST.get('max-'+str(sub.subject)) is not '' else '0'
            stuob = result.objects.filter(exam = examid,student=stuid,subject=sub.subject.id)
            if stuob.exists():
                stuob = stuob[0]
                stuob.obtain_marks = obmarks
                stuob.max_marks = mxmarks
            else:
                stuob = result(exam=examobj,student = studentregister.objects.get(id=stuid), subject= subject.objects.get(subject=str(sub.subject)),obtain_marks = obmarks,max_marks= mxmarks)
            stuob.save()
        Thread(target=sendresult, args=(request,)).start()
        messages.success(request,"Result is Updated Successfully")
        return redirect(request.get_full_path())
    resultobj = result.objects.filter(student=stuid,exam=examid)
    if resultobj.exists():
        from django.db.models import Sum
        from myapp.resultopration import per
        total = resultobj.aggregate(Sum('obtain_marks'),Sum('max_marks'))
        res = per(list(total.values())[0],list(total.values())[1],resultobj)
        return render(request,'staff/view-result.html',{'mainresult':resultobj,'total':res})
    if std is not None:
        classob = Class.objects.filter(standard=std.id)
        stuob = result.objects.filter(exam = examid)
        if stuob.exists():
            res = zip(classob,stuob)
        else:
            res = zip(classob,range(0,len(classob)))
        return render(request,'staff/view-result.html',{'result':res})
        
def deleteresult(request):
    exam = request.GET.get('exam')
    stuid = request.GET.get('stuid')
    stuob= studentregister.objects.get(id = stuid)
    date = request.GET.get('date')
    if exam is not None and stuid is not None and date is not None:
        resultobj = result.objects.filter(exam=exam,student = stuid)
        for data in resultobj:
            data.delete()        
        return redirect('mystudent')
def classes(request):
    clas = request.GET.get('id')
    delete = request.GET.get('delete')
    subob = Class.objects.filter(standard = clas)
    std = request.GET.get('standard')
    if request.method == "POST":
        form  = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Classes Is Added Successfully")
        else:
            return render(request,'staff/classes.html',{'subjects':subob,'form':form})
        return redirect(request.get_full_path())
    if delete is not None:
        messages.success(request,"Deleted Successfully....")
        Class.objects.get(id=delete).delete()
        return redirect(request.path+'?id='+clas)
    if clas is not None:
        form  = ClassForm(initial={'standard': clas})
        return render(request , 'staff/classes.html',{'subjects':subob or True,'form':form })
    form = standardForm()
    if std is not None:
        form = standardForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            classob = standard.objects.all()
            return render(request , 'staff/classes.html',{'classes':classob,'formstd':form})
    classob = standard.objects.all()
    return render(request , 'staff/classes.html',{'classes':classob,'formstd':form })
def subjects(request):
    if request.method=='POST':
        form = subjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Subject is Added Successfully.....")
            return redirect('subjects')
        else:
            subob = subject.objects.all()
            return render(request,'staff/subjects.html',{'subjects':subob,'subform':form})
    delete = request.GET.get('delete')
    sub= request.GET.get('subject')
    id = request.GET.get('id')
    if delete is not None:
        subject.objects.get(id=delete).delete()
        messages.success(request,"Deleted Successfully....")
        return redirect(request.path)
    if sub is not None and id is not None:
        subob = subject.objects.get(id=id)
        subob.subject = sub
        subob.save()
        return redirect('subjects')
    subob = subject.objects.all()
    subform = subjectForm()
    return render(request,'staff/subjects.html',{'subjects':subob,'subform':subform})

def users(request):
    if request.user.is_superuser:
        form = userRegister()
        form1 = StaffRegister()
        if request.method =="POST":
            form = userRegister(request.POST)
            form1 = StaffRegister(request.POST)
            if form1.is_valid and form.is_valid:
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
                return redirect('managestaff')
            else:
                users = staffregister.objects.all()
                return render(request,'staff/users.html',{'users':users,'forms':[form,form1]})
        users = staffregister.objects.all()
        return render(request,'staff/users.html',{'users':users,'forms':[form,form1]})
    return redirect('staff')
def manageattendance(request):
    classid = request.GET.get('id')
    date = request.GET.get('date')
    if request.method == "POST":
        date = request.POST['attendance_date']
        classid = request.POST['classid']
        stulist = studentregister.objects.filter(standard=classid)
        for stu in stulist:
            fattend = studentAttendance.objects.filter(standard=classid,student=stu.id,date=date)
            if fattend.exists():
                fattend = fattend[0]
            else:
                fattend = studentAttendance(standard=standard.objects.get(id=classid),student=studentregister.objects.get(id=stu.id),date = date)
            fattend.attend = request.POST.get('student'+str(stu.id)) == 'on'
            fattend.save()
        messages.success(request,"attendance of date:" + str(date)+ " is saved successfully")
        return redirect('manageattendance')
    if classid is not None and date is not None:
        fattend = studentAttendance.objects.filter(standard=classid,date=date)
        if fattend.exists():
            stulist = fattend
            studata = []
            for data in stulist:
                res = {
                    'stuid' : data.id,
                    'stuname' : data.student.user.first_name + " "+data.student.user.last_name,
                    'attend': data.attend
                }
                studata.append(res)
        else:
            stulist = studentregister.objects.filter(standard=classid)
            studata = []
            for data in stulist:
                res = {
                    'stuid' : data.id,
                    'stuname' : data.user.first_name + " "+data.user.last_name,
                    'attend': False
                }
                studata.append(res)
        studata = json.dumps(studata)
        return HttpResponse(studata)
    classes = standard.objects.all()
    return render(request,'staff/manageattendance.html',{"classes":classes})
def sessionmanagement(request):
    session = managesession.objects.all()
    form = managesessionForm()
    if request.method=="POST":
        form = managesessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('managesession')
    return render(request,'staff/sessionmanagement.html',{"session":session,'form':form})
def managestudentleave(request):
    leaveid = request.GET.get('student')
    status =  request.GET.get('status')
    if leaveid is not None and status is not None:
        leaveob =leavestudent.objects.get(id=leaveid)
        leaveob.leave_status = int(status)
        leaveob.save()
        messages.success(request,"leave status is succesfully changed")
        return redirect('managestudentleave')
    leaveitems = leavestudent.objects.all()
    return render(request,'staff/studentleave.html',{"leaves":leaveitems})
def myprofile(request):
    user = staffregister.objects.get(user=request.user)
    form = StaffRegister(instance=user)
    form1= userRegister(instance=request.user)
    if request.method == "POST":
        form = StaffRegister(request.POST,instance=user)
        if form.is_valid():
            form.save()
        messages.success(request, "Profile is updated succesfully")
        cpath = request.POST.get('cpath') or 'staff'
        return redirect(cpath)
    resp = render_block_to_string('staff/profile.html','profile',{'student':user,'form':form,'form1':form1},request)
    return HttpResponse(resp)
    # return render(request,'staff/profile.html',{'student':user,'form':form,'form1':form1})
def schoolinfo(request):
    if request.user.is_superuser:
        schoolinfo = schoolifo.objects.all()[0]
        if request.method=="POST":
            form = schoolinfoForm(request.POST,request.FILES,instance=schoolinfo)
            if form.is_valid():
                form.save()
                messages.success(request, "school information is updated successfully   ")
                return redirect('schoolinfo')
        form = schoolinfoForm(instance=schoolinfo)
        return render(request,'staff/schoolinfo.html',{"form":form})
    return redirect('staff')