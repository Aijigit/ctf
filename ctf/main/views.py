from .models import Task
from django.shortcuts import render

def index(request):
    return render(request, "index.html", {})


# tasks view
def task(request):
    object = Task.objects.all()
    count = Task.objects.all().count()
    context = {
        "tasks" : object,
        "count" : count
    }

    return render(request, "task.html", context)


def task_1(request):
    return render(request, 'tasks/task-1.html', {})