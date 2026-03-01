from django.shortcuts import HttpResponse
from django.template import loader
from .models import Stud
# Create your views here.

def members(request):
    studs=Stud.objects.all().values()
    template=loader.get_template("student_records.html")
    context={
        'studs':studs,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    stud1=Stud.objects.get(id=id)
    template=loader.get_template("details.html")
    context={
        'stud1':stud1,
    }
    return HttpResponse(template.render(context,request))



