from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from app.models import Todo
from django.http import HttpRequest, HttpResponse


def todos(request: HttpRequest) -> HttpResponse:
    completed_filter = request.GET.get('filter')
    if completed_filter == 'ACTIVE':
        todos = Todo.objects.filter(completed=False)
    elif completed_filter == 'COMPLETED':
        todos = Todo.objects.filter(completed=True)
    else:
        todos = Todo.objects.all()
    return render(request, 'app/todos.dhtml', {'todos': todos})


def create_todo(request: HttpRequest) -> HttpResponse:
    try:
        Todo.objects.create(title=request.POST.get('title'))
    except:
        print(request.POST.get('title'))
    return redirect(reverse('app:todos'))


def toggle_editing(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    todo.editing = not todo.editing
    todo.save()
    return redirect(reverse('app:todos'))


def toggle_completed(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect(reverse('app:todos'))


def new_title(request: HttpRequest, id: int) -> HttpResponse:
    print(request.POST)
    todo = get_object_or_404(Todo, id=id)
    todo.title = request.POST.get('title', todo.title)
    todo.editing = False
    todo.save()
    return redirect(reverse('app:todos'))


def delete_todo(request: HttpRequest, id: int) -> HttpResponse:
    Todo.objects.filter(id=id).delete()
    return redirect(reverse('app:todos'))
