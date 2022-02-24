from django.db import models

from apps.main.models import BaseModel


class Department(BaseModel):
    """

    """

    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self) -> str:
        return self.name
