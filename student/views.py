from django.shortcuts import render,redirect
from myapp.verify import create_token,verify_token
from django.core import serializers
from . models import studentregister,leavestudent
from staff.models import studentAttendance,examtype,result
from django.contrib import messages
from staff.models import staffregister,Class
from django.contrib.auth.models import User
from myapp.forms import StudentRegister,userRegister
# Create your views here.
def student(request):
    res = {}
    if request.user.studentregister_set.all()[0].status == False:
        res['verify'] = 'notverifyed'
    # data = serializers.serialize( "python",studentregister.objects.filter(user=request.user.id))
    # res['data'] = data
    res['totalattendance'] = studentAttendance.objects.filter(student=request.user.studentregister_set.all()[0].id).count()
    res['present'] = studentAttendance.objects.filter(student=request.user.studentregister_set.all()[0].id,attend=True).count()
    res['absent'] = res['totalattendance'] - res['present']
    res['totalsub'] = Class.objects.filter( standard=request.user.studentregister_set.all()[0].standard).count()
    return render(request,'student/student.html',res)

def test(request):
    li = [User,studentregister,staffregister]
    for m in li:
        pass
def viewresult(request):
    examid= request.GET.get('exam')
    stuid= request.GET.get('stuid')
    if examid is not None and stuid is not None:
        resultobj = result.objects.filter(exam=examid,student=stuid)
        from django.db.models import Sum
        from myapp.resultopration import per
        total = resultobj.aggregate(Sum('obtain_marks'),Sum('max_marks'))
        res = per(list(total.values())[0],list(total.values())[1],resultobj)
        return render(request,'student/view-result.html',{'mainresult':resultobj,'total':res})
    user = studentregister.objects.get(user=request.user)
    exams = examtype.objects.filter(Class=user.standard)
    return render(request,'student/view-result.html',{'exams':exams})
def viewattendance(request):
    if request.method == "POST":
        user = studentregister.objects.get(user=request.user)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        attendancedata = studentAttendance.objects.filter(student=user.id,date__range=(start_date,end_date))
        return render(request, 'student/showattendance.html',{"attendance_reports": attendancedata})
    return render(request,'student/viewattendance.html',{})
def myprofile(request):
    user = studentregister.objects.get(user=request.user)
    form = StudentRegister(instance=user)
    form1= userRegister(instance=request.user)
    if request.method == "POST":
        form = StudentRegister(request.POST,instance=user)
        form1= userRegister(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
        messages.success(request, "Profile is updated succesfully")
        return redirect('studentprofile')
    return render(request,'student/profile.html',{'student':user,'form':form,'form1':form1})
def studentleave(request):
    user = studentregister.objects.get(user=request.user)
    if request.method=="POST":
        leave_date= request.POST['leave_date']
        leave_message= request.POST['leave_message']
        checkleave = leavestudent.objects.filter(student_id=user,leave_date=leave_date)
        if checkleave.exists():
            messages.error(request, "Your request for leave on "+ str(leave_date) +" is already made")
            return redirect('studentleave')
        leavestudent(student_id=user,leave_date=leave_date,leave_message=leave_message).save()
        messages.success(request, "Your request for leave is Successfully submit")
        return redirect('studentleave')
    if request.GET.get('delete') is not None:
        leavestudent.objects.get(id=request.GET.get('delete')).delete()
        messages.success(request, "Your request for leave is Deleted")
        return redirect('studentleave')
    leaveob = leavestudent.objects.filter(student_id=user.id)
    return render(request,'student/applyforleave.html',{'leave_data':leaveob})
