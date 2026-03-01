from django.contrib import admin
from enroll.models import student


# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('id','studid','name','email','password')
    