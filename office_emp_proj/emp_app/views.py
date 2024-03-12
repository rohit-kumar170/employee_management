from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request,'index.html')
@login_required
def all_emp(request):
    emps=Employee.objects.all()
    
    #paginator
    paginator=Paginator(emps,5)
    page=request.GET.get('page')
    emps=paginator.get_page(page)
    return render(request,'all_emp.html',context={'emps':emps})

@login_required
def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['department'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_dt=datetime.now())
        new_emp.save()
        return HttpResponse("<h3>New Employee added sucessfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Error Occured!, Employee not added")
@login_required
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Sucessfully")
        except:
            return HttpResponse("Pleaseb select valid Emp ID")


    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)
@login_required
def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['department']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        
        context={
            'emps':emps
        }

        return render(request,'all_emp.html',context)
    
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An Execution Error!")


