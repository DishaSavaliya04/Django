from django.shortcuts import render,redirect
from .models import Employee


# Create your views here.
def emp_list(request):
    emp=Employee.objects.all()
    return render(request,"emp_details.html",{"emp":emp})

def emp_add(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        salary=request.POST.get("salary")
        department=request.POST.get("department")
        Employee.objects.create(name=name,email=email,salary=salary,department=department)
        return redirect("emp_list")
    return render(request,"add.html")

def emp_update(request,id):
    emp=Employee.objects.get(id=id)
    if request.method == "POST":
        emp.name=request.POST.get('name')
        emp.email=request.POST.get('email')
        emp.salary=request.POST.get('salary') 
        emp.department=request.POST.get("department")
        emp.save()
        return redirect('emp_list')
    return render(request,'update.html',{'emp':emp})

def emp_delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('emp_list')

def emp_action(request):
    if request.method == "POST":
        select = request.POST.getlist("selected")
        action = request.POST.get("action")
        
        if select:
            if action == "delete":
                Employee.objects.filter(id__in=select).delete()

            elif action == "update":
                name = request.POST.get("name")
                email = request.POST.get("email")
                salary = request.POST.get("salary")
                department = request.POST.get("department")
                employee=Employee.objects.filter(id__in=select)
                for emp in employee:
                    if name:
                        emp.name = name
                    if email:
                        emp.email = email
                    if salary:
                        emp.salary = salary
                    if department:
                        emp.department = department
                    emp.save()

        return redirect("emp_list")