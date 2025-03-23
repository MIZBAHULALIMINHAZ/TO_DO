

from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks= Task.objects.filter(is_completed=False).order_by('Last_date')
    completed_task = Task.objects.filter(is_completed=True).order_by('Last_date')
    context = {
        'tasks' : tasks,
        'completed_tasks':completed_task
    }
    return   render(request, 'home.html', context)