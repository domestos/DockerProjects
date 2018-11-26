from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


def index(request):
    return render(request, 'employees/employees.html')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer
