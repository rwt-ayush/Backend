import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(
                    max_length=254,
                    unique=True,
                    validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]
                )),
                ('phone', models.CharField(
                    max_length=10,
                    validators=[django.core.validators.RegexValidator(r'^\d{10}$', message='Enter a valid 10-digit mobile number.')]
                )),
                ('high_school_marks', models.DecimalField(
                    max_digits=5,
                    decimal_places=2,
                    validators=[
                        django.core.validators.MinValueValidator(0.0, message='Marks cannot be less than 0.'),
                        django.core.validators.MaxValueValidator(100.0, message='Marks cannot exceed 100.')
                    ]
                )),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
            ],
        ),
    ]
