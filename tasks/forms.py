from django import forms
from .models import Task

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
