from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=122,null=False)
    location=models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=122,null=False)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=122,null=False)
    last_name=models.CharField(max_length=122)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()
    
    def __str__(self) -> str:
        return "%s %s"%(self.first_name,self.last_name)
