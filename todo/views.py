from . models import Task
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def addTask(request):
    task=request.POST['task']
    taskd=request.POST['taskd']
    Task.objects.create(task=task, Last_date=taskd)
    return redirect('home')