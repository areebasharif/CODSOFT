from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.urls import reverse

def home(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            new_task = Todo(task=task)
            new_task.save()
            return redirect('/')

    return render(request, 'home.html', {'todos': todos})

def deletion(request, pk):
    task = get_object_or_404(Todo, id=pk)
    task.delete()
    return redirect('/')
