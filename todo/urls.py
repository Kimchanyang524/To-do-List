from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="todo-index"),
    path("add-todo/", views.add_todo, name="add-todo"),
    path("remove-todo/<int:pk>", views.remove_todo, name="remove-todo"),
]
