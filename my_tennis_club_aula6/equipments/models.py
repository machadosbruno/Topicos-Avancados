from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    register_number = models.IntegerField(null=False)
    register_date = models.DateField(null=False)