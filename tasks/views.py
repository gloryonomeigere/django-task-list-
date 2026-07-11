from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "tasks/index.html")

def add(request):
    return render(request, "tasks/add_task.html")