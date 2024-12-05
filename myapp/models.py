from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Memory(models.Model):
    photo = models.ImageField(upload_to='memories/')
    date = models.DateField()

    def __str__(self):
        return f"Memory for {self.date}"