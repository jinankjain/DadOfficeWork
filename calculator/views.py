from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.conf import settings
from django.conf.urls.static import static
from calculator.models import *
from datetime import datetime
import json
import time
import requests
import os
from readAttendance import *

def index(request):
    return render(request, 'index.html')

def handle_file_upload(f, name):
    fileName = os.path.join(settings.BASE_DIR, "calculator", "attendanceSheet", name)
    with open(fileName, 'w+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def submit(request):
    filename = str(request.POST.get('date')).replace('/','')
    filename = filename + ".csv"
    handle_file_upload(request.FILES.get('attend'), filename)
    filename = os.path.join(settings.BASE_DIR, "calculator", "attendanceSheet", filename)
    d, salary = readAttendance(filename)
    #salary = json.dumps(salary)
    employees = Employee.objects.all()
    for e in employees:
        s = Salary(date=datetime.strptime(d, '%m/%d/%Y').strftime('%Y-%m-%d'), noOfHours = salary.get(str(e.employeeId)), employee=e)
        s.save()
    sal = Salary.objects.filter(date = datetime.strptime(d, '%m/%d/%Y').strftime('%Y-%m-%d'))
    return render(request, 'submit.html', {'salary':sal})

def viewSalary(request):
    dateFrom = request.POST.get('dateFrom')
    dateFrom = datetime.strptime(dateFrom, '%m/%d/%Y').strftime('%Y-%m-%d')
    dateTo = request.POST.get('dateTo')
    dateTo = datetime.strptime(dateTo, '%m/%d/%Y').strftime('%Y-%m-%d')
    employees = Employee.objects.all()
    totalSalary = {}
    for e in employees:
        totalSalary.update({str(e.employeeId):0.0})
    salary = Salary.objects.filter(date__range=[dateFrom, dateTo])
    for e in employees:
        for s in salary:
            if(e.employeeId==s.employee.employeeId):
                totalSalary[str(e.employeeId)] = totalSalary[str(e.employeeId)] + s.noOfHours 
    totalSalary = json.dumps(totalSalary)
    return render(request, 'view.html', {'employees':employees, 'totalSalary':totalSalary})
