from operator import mod
from statistics import mode
from django.db import models

from apps.employees.models import Department
from apps.main.models import BaseModel


class Employee(BaseModel):
    """

    """

    GENDER_CHOICES = [
    ('F', 'Female'),
    ('M', 'Male'),
    ('-', 'Prefer Not To Say')
]

    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees"
    )
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default=GENDER_CHOICES[2][0])
    hire_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='employees/avatars/', blank=True, null=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self) -> str:
        return self.name
