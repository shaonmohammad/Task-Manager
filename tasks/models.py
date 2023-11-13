from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field

    def __str__(self):
        return self.title


class TaskImage(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='images')
    images = models.FileField(upload_to='task_images/')
