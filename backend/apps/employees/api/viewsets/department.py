from rest_framework import viewsets

from apps.employees.api.serializers import DepartmentSerializer
from apps.employees.models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
