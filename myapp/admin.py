from django.contrib import admin
from .models import Project, Tasks

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tasks, TaskAdmin)