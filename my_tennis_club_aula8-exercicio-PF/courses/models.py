from django.db import models
from instructors.models import Instructor

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)