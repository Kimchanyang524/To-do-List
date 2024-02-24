from django.db import models


# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
