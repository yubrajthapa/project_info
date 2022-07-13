from django.db import models

# Create your models here.
from email.policy import default
from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    is_verified = models.BooleanField(null=True, default=False)
    verification_code = models.CharField(max_length=8)


    class Meta:
        db_table = "student_detail"


class AcademicDetail(models.Model):
    org_name = models.CharField(max_length=100)
    org_location = models.CharField(max_length=200)
    academic_degree = models.CharField(max_length=200)
    secured_marks = models.CharField(max_length=200)
    position_category = models.CharField(max_length=200)
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = "academic_detail"


class TrainingDetail(models.Model):
    org_name = models.CharField(max_length=200)
    titile = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    student = models.ForeignKey(StudentDetail, on_delete = models.CASCADE)

    class Meta:
        db_table = "training_detail"
