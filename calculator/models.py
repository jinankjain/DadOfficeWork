from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    employeeId = models.IntegerField(primary_key=True)
    employeeName = models.CharField(max_length=200)
    ratePerHour = models.FloatField()
    company = models.CharField(max_length=200, default="Bhairav Offset")
    department = models.CharField(max_length=200)

    def __unicode__(self):
        return self.employeeName

class Salary(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateField()
    noOfHours = models.FloatField()

    def __unicode__(self):
        return self.employee.employeeName

class Attendance(models.Model):
    date = models.DateTimeField()
    attendance = models.FileField(upload_to="attendanceSheet")

    def __unicode__(self):
        return str(self.date)
