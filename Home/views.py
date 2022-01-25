from django.shortcuts import render,HttpResponse
from Home.models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'home.html')

def AllEmployees(request):
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
    return render(request,'all.html',context)

def AddEmployee(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emps=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emps.save()
        return HttpResponse("Employee Details Saved")
    elif request.method=='GET':
        return render(request,'add.html')
    else:
        return HttpResponse("Error")

def RemoveEmployee(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_deleted=Employee.objects.get(id=emp_id)
            emp_to_be_deleted.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse("Error")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove.html',context)

def FilterEmployees(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        context={
            'emps':emps
        }
        return render(request,'all.html',context)
    elif request.method=='GET':
         return render(request,'filter.html')
    else:
        return HttpResponse('Error')