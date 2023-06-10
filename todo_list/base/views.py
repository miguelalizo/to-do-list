from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import login

from .models import Task
from .user_based_generic_views import UserBasedList, UserBasedCreate, UserBasedDelete, UserBasedDetail, UserBasedUpdate

class RegisterPage(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    template_name = 'base/register.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.redirect_name)
        return super(RegisterPage, self).get(*args, **kwargs)

class UserTaskList(UserBasedList):
    model = Task
    context_object_name = 'tasks'
    
class UserTaskDetail(UserBasedDetail):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class UserTaskCreate(UserBasedCreate):
    model = Task
    fields = ['title', 'description', 'complete'] 
    success_url =  reverse_lazy('tasks')

class UserTaskUpdate(UserBasedUpdate):
    model = Task
    fields = ['title', 'description', 'complete'] 
    success_url = reverse_lazy('tasks')

class UserTaskDelete(UserBasedDelete):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

def task_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.complete = not task.complete
    task.save()
    return redirect('tasks')
