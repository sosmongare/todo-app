from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')

def mark_task_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
