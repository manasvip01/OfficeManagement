from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('AllEmployees', views.AllEmployees,name='AllEmployees'),
    path('AddEmployee', views.AddEmployee,name='AddEmployee'),
    path('RemoveEmployee', views.RemoveEmployee,name='RemoveEmployee'),
    path('RemoveEmployee/<int:emp_id>', views.RemoveEmployee,name='RemoveEmployee'),
    path('FilterEmployees', views.FilterEmployees,name='FilterEmployee'),
]
