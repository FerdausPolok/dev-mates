from django.db import models
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import datetime

User = get_user_model()


# Create your models here.


class Result(models.Model):
    result_type = (
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('bsc', 'BSC'),
        ('bba', 'BBA'),
        ('ba', 'BA'),
        ('others', 'OTHERS'),
    )

    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result_applicant')
    type = models.CharField(choices=result_type, max_length=20, default='others')
    sub_or_group = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=4)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'result of {self.applicant}'