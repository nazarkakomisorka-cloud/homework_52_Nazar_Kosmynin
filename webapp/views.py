from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, status_choices

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'webapp/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'webapp/task_detail.html', {'task': task})

def task_add(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        details = request.POST.get('details')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date') or None
        Task.objects.create(description=description, details=details, status=status, due_date=due_date)
        return redirect('task_list')
    return render(request, 'webapp/task_add.html', {'status_choices': status_choices})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
