from django.db import models


class Student(models.Model):
    students_number = models.PositiveBigIntegerField()
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    fields_of_study = models.CharField(max_length=30)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student:{self.first_name} {self.last_name}'



