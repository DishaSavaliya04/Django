from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def stud_list(request):
    stud1=Student.objects.all()
    return render(request,'stud/student_list.html',{'stud1':stud1})

def create_list(request):
    if request.method=="POST":
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        marks=request.POST.get('marks') 

        Student.objects.create(name=name,rollno=rollno,marks=marks)
    return redirect('stud_list') 

def delete_list(request,id):
    stud1=Student.objects.get(id=id)
    stud1.delete()
    return redirect('stud_list')

def update_list(request,id):
    if request.method == "POST":
        stud1=Student.objects.get(id=id)
        stud1.name=request.POST.get('name')
        stud1.rollno=request.POST.get('rollno')
        stud1.marks=request.POST.get('marks') 
        stud1.save()
        return redirect('stud_list')
    return render(request,'stud/update.html',{'Student':Student})

