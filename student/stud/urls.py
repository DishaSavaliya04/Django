from django.urls import path
from . import views

urlpatterns = [
    path('stud1/', views.members, name='stud1'),
    path("stud/details/<int:id>",views.details,name="details"),

]