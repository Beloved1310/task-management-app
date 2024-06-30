from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User

# HTML Views
@login_required
def frontpage(request):
    return render(request, 'base.html')

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

# API Views
@login_required
def api_tasks(request):
    status = request.GET.get('status', None)
    if status:
        tasks = Task.objects.filter(status=status)
    else:
        tasks = Task.objects.all()
    
    task_list = list(tasks.values())
    
    status_counts = {
        'In Progress': Task.objects.filter(status='In Progress').count(),
        'Completed': Task.objects.filter(status='Completed').count(),
        'Overdue': Task.objects.filter(status='Overdue').count(),
    }
    
    return JsonResponse({'tasks': task_list, 'status_counts': status_counts})
