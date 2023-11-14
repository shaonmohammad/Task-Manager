from django.contrib import admin

# Register your models here.
from .models import Task, TaskImage


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'is_complete')
    ordering = ('priority',)


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskImage)
