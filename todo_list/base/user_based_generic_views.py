from typing import Any
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserBasedList(LoginRequiredMixin, ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = context[self.context_object_name].filter(user=self.request.user)
        context['count'] = context[self.context_object_name].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context[self.context_object_name] = context[self.context_object_name].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context

class UserBasedDetail(LoginRequiredMixin, DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """

class UserBasedCreate(LoginRequiredMixin, CreateView):
    """
    Sub-class the CreateView to pass the request to the form.
    """

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserBasedCreate, self).form_valid(form)

class UserBasedUpdate(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form.
    """

    def get_queryset (self) :
        print ('update get _queryset called')
        # Limit a User to only modifying their own data.
        qs = super(UserBasedUpdate, self).get_queryset()
        return qs.filter(user=self.request.user)

class UserBasedDelete(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to pass the request to the form.
    """

    def get_queryset (self) :
        print ('update get _queryset called')
        # Limit a User to only delete their own data.
        qs = super(UserBasedDelete, self).get_queryset()
        return qs.filter(user=self.request.user)
