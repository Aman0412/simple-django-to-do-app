from django import forms
from todo.models import ToDoItem

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'completed']