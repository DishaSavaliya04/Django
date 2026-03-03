from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):

    list_display=("name","email","salary","department",)

admin.site.register(Employee,EmployeeAdmin)

