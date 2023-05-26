from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoList
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoList(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Todo.objects.all
            messages.success(request, ("Item has been added to List"))
            return render(request, "home.html", {"all_items": all_items})
    else:
        all_items = Todo.objects.all
        return render(request, "home.html", {"all_items": all_items})
    
def edit(request, todo_id):
    if request.method == 'POST':
        item = Todo.objects.get(pk=todo_id)
        form = TodoList(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item has been edited"))
            return redirect("home")
        
        return redirect("home")

    else:
        item = Todo.objects.get(pk=todo_id)
        return render(request, "edit.html", {"item": item})

def delete(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.delete()
    messages.success(request, ("Item has been deleted"))
    return redirect("home")

def cross_off(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.completed = True
    item.save()
    return redirect("home")

def uncross(request, todo_id):
    item = Todo.objects.get(pk=todo_id)
    item.completed = False
    item.save()
    return redirect("home")
