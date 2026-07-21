from django.shortcuts import render, redirect, get_object_or_404
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

def update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("task_list")

    return render(request, "tasks/create_task.html", {
        "form": form
    })