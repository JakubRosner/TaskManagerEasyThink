from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="task", null=True)
    title = models.CharField(max_length=32, null=True)
    description = models.TextField(max_length=255, null=True)
    done = models.BooleanField()

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return str(self.title)
