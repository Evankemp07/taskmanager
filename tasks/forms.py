from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Create a password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

        # Remove help text
        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = True

class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ["name"]