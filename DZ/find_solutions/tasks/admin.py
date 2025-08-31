from django.contrib import admin
from .models import Task, Lines, Place, Message


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Lines)
admin.site.register(Place)
admin.site.register(Message)
