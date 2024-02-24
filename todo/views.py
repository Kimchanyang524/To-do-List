from django.shortcuts import render, redirect
from .models import TodoItem


def index(request):
    context = {"todo_items": TodoItem.objects.all()}
    return render(request, "todo/index.html", context)


def add_todo(request):
    todo = request.POST["todo"]
    TodoItem(content=todo).save()
    return redirect("todo-index")
