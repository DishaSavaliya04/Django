from django.urls import path
from  .import views

urlpatterns=[
    path('',views.emp_add,name="emp_add"),
    path("list/",views.emp_list,name="emp_list"),
    path('update/<int:id>/',views.emp_update,name="emp_update"),
    path('delete/<int:id>/',views.emp_delete,name="emp_delete"),
]
