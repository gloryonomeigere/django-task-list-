from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index, name="task_list"),
    path("create/", views.create, name="task_create"),
]