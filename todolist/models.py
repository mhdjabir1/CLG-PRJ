from django.db import models
from django.utils import timezone
from category.models import Category
from django.contrib.auth.models import User

class Priority(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'

class Status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'

class TodoList(models.Model): 
    title = models.CharField(max_length=250, verbose_name="Task Title") 
    content = models.TextField(blank=True, null=True, verbose_name="Description") 
    created = models.DateField(default=timezone.now, verbose_name="Created On") 
    time = models.TimeField(null=True, blank=True, verbose_name="Time")
    due_date = models.DateField(null=True, blank=True, verbose_name="Due Date") 
    category = models.ForeignKey(Category, default=None, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Category") 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User")
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM, verbose_name="Priority")
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, verbose_name="Status")
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True, verbose_name="Attachment")

    class Meta:
        ordering = ["-created"]
        verbose_name = "To-Do Task"
        verbose_name_plural = "To-Do Tasks"
   
    def __str__(self):
        return f"{self.title} ({self.status})"
