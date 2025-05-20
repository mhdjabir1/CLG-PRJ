from django.contrib import admin
from .models import TodoList

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority', 'status', 'due_date')
    list_filter = ('priority', 'status', 'category', 'due_date')
    search_fields = ('title', 'content', 'user__username')
    ordering = ('-created',)

