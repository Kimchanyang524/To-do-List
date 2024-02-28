from django.shortcuts import render, redirect
from .models import TodoItem


def index(request):
    context = {"todoitems": TodoItem.objects.all()}
    return render(request, "todo/index.html", context)


def add_todo(request):
    todo = request.POST["todo"]
    TodoItem(content=todo).save()
    return redirect("todo-index")


def remove_todo(request, pk):
    TodoItem.objects.get(id=pk).delete()
    return redirect("todo-index")
