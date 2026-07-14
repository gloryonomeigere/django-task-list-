from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    context = {
       "tasks": tasks
    }
    return render(request, "tasks/index.html", context)

def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})