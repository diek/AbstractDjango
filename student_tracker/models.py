from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    is_owner = models.BooleanField(null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


class Teacher(CommonInfo):
    hire_date = models.DateField()
