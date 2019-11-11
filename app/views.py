from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from app.models import Todo
from django.http import HttpRequest, HttpResponse


# Renders home page with the correct todo's passed
# in to the context.


def todos(request: HttpRequest) -> HttpResponse:
    completed_filter = request.GET.get("filter")
    if completed_filter == "ACTIVE":
        todos = Todo.objects.filter(completed=False)
    elif completed_filter == "COMPLETED":
        todos = Todo.objects.filter(completed=True)
    else:
        todos = Todo.objects.all()
    return render(request, "app/todos.dhtml", {"todos": todos})


# Creates new todo object with the provided title,
# Redirects to home page.


def create_todo(request: HttpRequest) -> HttpResponse:
    try:
        Todo.objects.create(title=request.POST.get("title"))
    except:
        print(request.POST.get("title"))
    return redirect(reverse("app:todos"))


# Toggles editing mode on an already existing todo.


def toggle_editing(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    todo.editing = not todo.editing
    todo.save()
    return redirect(reverse("app:todos"))


# Toggles completed status on already existing todo.


def toggle_completed(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect(reverse("app:todos"))


# If todo is in editing mode, allows user to raname the title of the
# selected todo.


def new_title(request: HttpRequest, id: int) -> HttpResponse:
    print(request.POST)
    todo = get_object_or_404(Todo, id=id)
    todo.title = request.POST.get("title", todo.title)
    todo.editing = False
    todo.save()
    return redirect(reverse("app:todos"))


# Deletes the selected todo from the database.


def delete_todo(request: HttpRequest, id: int) -> HttpResponse:
    Todo.objects.filter(id=id).delete()
    return redirect(reverse("app:todos"))


# This was random testing for some in class work
# that I just shoved in to this repository since it was already up
# and running.


def will_view(request):
    print(request.GET["color"])
    if request.GET["color"] == "blue":
        return HttpResponse("Thats my fav")
    else:
        return HttpResponse("Not my fav")


def add_numbers(request):
    result = int(request.GET["x"]) + int(request.GET["y"])
    return HttpResponse(str(result))
