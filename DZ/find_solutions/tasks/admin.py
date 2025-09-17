from django.contrib import admin
from .models import Task, Lines, Place, Message
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class TaskAdminForm(forms.ModelForm):
    memo = forms.CharField(widget=CKEditorUploadingWidget)
    decision = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Task
        fields = "__all__"


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    readonly_fields = ('created',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Lines)
admin.site.register(Place)
admin.site.register(Message)
