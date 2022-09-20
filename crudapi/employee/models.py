from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    emp_id = models.BigIntegerField()

    def __str__(self):
        return self.name