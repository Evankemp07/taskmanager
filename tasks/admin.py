from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import path
import pandas as pd
from django.contrib import messages
from django.utils.html import format_html
from django.http import HttpResponse
from django_object_actions import DjangoObjectActions, action
from .models import Task, TaskList

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class TaskListInline(admin.TabularInline): 
    model = TaskList
    extra = 1  

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    inlines = [TaskListInline]

class TaskListAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)
    inlines = [TaskInline] 

    @action(label="Upload Tasks", description="Upload tasks from a file")
    def upload_tasks_action(self, request, obj):
        return redirect("/admin/tasks/tasklist/upload-tasks/")

    @action(label="Export Tasks", description="Export all tasks to a CSV file")
    def export_tasks_action(self, request, obj):
        tasks = Task.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tasks_export.csv"'
        df = pd.DataFrame(list(tasks.values('task_list__user__username', 'task_list__name', 'title', 'completed')))
        df.rename(columns={
            'task_list__user__username': 'Username',
            'task_list__name': 'Task List',
            'title': 'Task',
            'completed': 'Completed'
        }, inplace=True)
        df.to_csv(response, index=False)
        return response

    @action(label="Clear All Tasks", description="Delete all tasks from the system")
    def clear_all_tasks_action(self, request, obj):
        Task.objects.all().delete()
        messages.success(request, "All tasks have been deleted successfully!")
        return redirect("/admin/tasks/tasklist/")

    @action(label="Download Template", description="Download a CSV template for uploading tasks")
    def download_template_action(self, request, obj=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tasks_template.csv"'
        df = pd.DataFrame(columns=["Username", "Task List", "Task", "Completed"])
        df.to_csv(response, index=False)
        return response

    change_actions = ('upload_tasks_action', 'export_tasks_action', 'clear_all_tasks_action') 
    changelist_actions = ('upload_tasks_action', 'export_tasks_action', 'clear_all_tasks_action')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-tasks/', self.admin_site.admin_view(self.upload_tasks), name="upload-tasks"),
            path('download-template/', self.admin_site.admin_view(self.download_template_action), name="download-template"),
        ]
        return custom_urls + urls

    def upload_tasks(self, request):
        if request.method == "POST" and request.FILES.get("task_file"):
            file = request.FILES["task_file"]
            try:
                if file.name.endswith(".csv"):
                    df = pd.read_csv(file)
                elif file.name.endswith(".xlsx"):
                    df = pd.read_excel(file)
                else:
                    messages.error(request, "Invalid file format. Upload a CSV or Excel file.")
                    return redirect("..")

                df.columns = df.columns.str.strip().str.lower()

                for _, row in df.iterrows():
                    username = str(row.get("username", "")).strip()
                    task_list_name = str(row.get("task_list", "")).strip()
                    task_title = str(row.get("task", "")).strip()
                    completed = str(row.get("completed", "false")).strip().lower() in ['true', '1', 'yes']
                    
                    if username and task_list_name and task_title:
                        user, created = User.objects.get_or_create(username=username, defaults={"email": f"{username}@example.com"})
                        if created:
                            user.set_password(f"{username}1234")
                            user.save()
                        task_list, _ = TaskList.objects.get_or_create(name=task_list_name, user=user)
                        task, task_created = Task.objects.get_or_create(title=task_title, task_list=task_list, defaults={"completed": completed})
                        if not task_created:
                            task.completed = completed
                            task.save()
                    else:
                        messages.error(request, f"Missing required fields in row: {row}")

                messages.success(request, "Tasks uploaded successfully!")
                return redirect("..")

            except Exception as e:
                messages.error(request, f"Error processing file: {e}")
                return redirect("..")

        return render(request, "admin/upload_tasks.html")

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'task_list')
    list_filter = ('completed', 'task_list', 'task_list__user')
    search_fields = ('title', 'task_list__name')

admin.site.unregister(User) 
admin.site.register(User, CustomUserAdmin) 
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)
