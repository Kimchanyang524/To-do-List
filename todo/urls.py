from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="todo-index"),
    path("add-todo/", views.add_todo, name="add-todo"),
]
