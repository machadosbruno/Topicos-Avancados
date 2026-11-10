from django.db import models
from plans.models import Plan

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ImageField(upload_to='members/', blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"