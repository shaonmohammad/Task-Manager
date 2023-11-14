from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
        'multiple': True
    }))

    class Meta:
        model = Task
        fields = ['title', 'description',
                  'due_date', 'is_complete', 'priority']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'due_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '7', 'placeholder': 'Enter the description'}),
            'priority': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select the priority'}),

        }
