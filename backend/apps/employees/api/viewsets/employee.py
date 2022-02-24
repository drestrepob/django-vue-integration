from rest_framework import viewsets

from apps.employees.api.serializers import EmployeeSerializer
from apps.employees.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
