from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MinValueValidator, MaxValueValidator
from student.models import Department


class StudentApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Enter a valid 10-digit mobile number.")]
    )
    high_school_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0.0, message="Marks cannot be less than 0."),
            MaxValueValidator(100.0, message="Marks cannot exceed 100.")
        ]
    )
    course = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
