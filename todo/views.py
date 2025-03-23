from . models import Task
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.
def addTask(request):
    task=request.POST['task']
    taskd=request.POST['taskd']
    Task.objects.create(task=task, Last_date=taskd)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    task_get=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task=request.POST['task']
        new_date=request.POST['Last_date']
        task_get.task=new_task
        task_get.Last_date=new_date
        task_get.save()
        return redirect('home')
    else :
        context ={
            'get_task': task_get,
        }
        return render(request,'edit_task.html',context)
    
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')