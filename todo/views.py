from django.shortcuts import render, redirect
from todo.models import *
from todo.forms import ToDoForm

# Create your views here.
def index(request):
    context = {}
    todos = ToDoItem.objects.all()
    form = ToDoForm()    
    
    context['todos'] = todos


    return render(request, 'main1.html', context)
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            ToDoItem.objects.create(title=title, completed=False)
    return redirect("index")

def delete_task(request, id):
    ToDoItem.objects.filter(id=id).delete()
    return redirect("index")