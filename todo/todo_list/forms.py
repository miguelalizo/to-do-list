from django import forms 
from .models import Todo

class TodoList(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["item", "completed"]