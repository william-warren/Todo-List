from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    editing = models.BooleanField(default=False)

    @property
    def if_toggle_completed(self) -> bool:
        return not self.completed
