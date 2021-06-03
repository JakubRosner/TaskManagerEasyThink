from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    FINISHED = [
        ('C', 'Completed'),
        ('T', 'To be done'),
    ]
    User = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="task", null=True)
    title = models.CharField(max_length=32, null=True)
    description = models.TextField(max_length=255, null=True)
    done = models.CharField(choices=FINISHED, max_length=1, null=True)

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")
        ordering = ['-done']

    def __str__(self):
        return str(self.title)
