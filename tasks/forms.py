# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
            'placeholder': 'Email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Confirm Password'
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
            'placeholder': 'Password'
        })
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea block w-full px-3 py-2 border border-gray-300 rounded-md',
                'placeholder': 'Description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select block w-full px-3 py-2 border border-gray-300 rounded-md'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select block w-full px-3 py-2 border border-gray-300 rounded-md'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input block w-full px-3 py-2 border border-gray-300 rounded-md',
                'type': 'date'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select block w-full px-3 py-2 border border-gray-300 rounded-md'
            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-select block w-full px-3 py-2 border border-gray-300 rounded-md'
            }),
        }
