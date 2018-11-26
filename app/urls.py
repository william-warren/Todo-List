from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path(
        'todo/',
        views.todos,
        name='todos', ),
    path(
        'todo/create/',
        views.create_todo,
        name='create', ),
    path(
        'todo/<int:id>/toggle_editing/',
        views.toggle_editing,
        name='toggle_editing', ),
    path(
        'todo/<int:id>/toggle_completed/',
        views.toggle_completed,
        name='toggle_completed', ),
    path(
        'todo/<int:id>/new-title',
        views.new_title,
        name='new-title', ),
    path(
        'todo/<int:id>/delete/',
        views.delete_todo,
        name='delete', )
]
