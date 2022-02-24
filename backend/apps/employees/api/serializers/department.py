from rest_framework import serializers

from apps.employees.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = Department
        fields = "__all__"
