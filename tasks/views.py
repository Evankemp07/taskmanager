from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm, CustomUserCreationForm
from .models import Task, TaskList
from .forms import TaskListForm
from django.http import JsonResponse


@login_required
def home(request):
    """Display all task lists on the home page."""
    task_lists = TaskList.objects.filter(user=request.user)
    return render(request, 'tasks/home.html', {'task_lists': task_lists})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    """Logs out user and redirects to logged-out page."""
    logout(request)
    return redirect('logged_out')

def logout_success(request):
    """Handles GET request for logout success page."""
    return render(request, 'tasks/logged_out.html')

@login_required
def add_task(request, list_id):
    """Add a task to a specific task list"""
    task_list = get_object_or_404(TaskList, id=list_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_list = task_list
            task.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form, "task_list": task_list})

@login_required
def edit_task(request, task_id):
    """Edit a task if it belongs to a task list owned by the user."""
    task = get_object_or_404(Task, id=task_id, task_list__user=request.user)  

    if request.method == "POST":
        if "delete" in request.POST:
            task.delete()
            return redirect("home")
        else:
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("home")

    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {"form": form, "task": task})


@login_required
def mark_completed(request, task_id):
    """Mark a task as completed if it belongs to a task list owned by the user."""
    task = get_object_or_404(Task, id=task_id, task_list__user=request.user)

    task.completed = True
    task.save()

    return redirect("home")  


@login_required
def task_lists(request):
    """View all task lists for the logged-in user"""
    lists = TaskList.objects.filter(user=request.user)
    return render(request, "tasks/task_lists.html", {"lists": lists})

@login_required
def create_task_list(request):
    """Create a new task list and redirect to home."""
    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            return redirect("home") 

    return redirect("home") 


@login_required
def task_list_detail(request, list_id):
    """View tasks inside a specific task list"""
    task_list = get_object_or_404(TaskList, id=list_id, user=request.user)
    tasks = task_list.tasks.all()
    return render(request, "tasks/task_list_detail.html", {"task_list": task_list, "tasks": tasks})

@login_required
def edit_task_list(request, list_id):
    """Edit a task list's name."""
    task_list = get_object_or_404(TaskList, id=list_id, user=request.user)

    if request.method == "POST":
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
            return redirect("home") 
    else:
        form = TaskListForm(instance=task_list)

    return render(request, "tasks/edit_task_list.html", {"form": form, "task_list": task_list})

@login_required
def delete_task_list(request, list_id):
    """Delete a task list if it belongs to the logged-in user."""
    task_list = get_object_or_404(TaskList, id=list_id, user=request.user)

    if request.method == "POST":
        task_list.delete()
        return redirect("home") 

    return render(request, "tasks/delete_task_list.html", {"task_list": task_list})

@login_required
def delete_task(request, task_id):
    """Delete a task if it belongs to the logged-in user."""
    task = get_object_or_404(Task, id=task_id, task_list__user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("home")

    return render(request, "tasks/delete_task.html", {"task": task})

def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)
