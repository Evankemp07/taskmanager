from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views 
from .views import user_logout, logout_success
from django.views.generic import TemplateView
from .views import health_check

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('logged-out/', logout_success, name='logged_out'),
    # path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path("task_lists/", views.task_lists, name="task_lists"),
    path("task_lists/create/", views.create_task_list, name="create_task_list"),
    path("task_lists/<int:list_id>/", views.task_list_detail, name="task_list_detail"),
    path("task_lists/<int:list_id>/add_task/", views.add_task, name="add_task"),
    path("task_lists/<int:list_id>/edit/", views.edit_task_list, name="edit_task_list"),
    path("task_lists/<int:list_id>/delete/", views.delete_task_list, name="delete_task_list"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path('serviceworker.js', TemplateView.as_view(template_name="serviceworker.js", content_type='application/javascript')),
    path("api/healthcheck/", health_check, name="health_check"),
]

