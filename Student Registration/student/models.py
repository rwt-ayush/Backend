from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
