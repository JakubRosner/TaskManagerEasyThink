from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404

from .models import Task
from .forms import SingUpForm, EditUserForm


class HomePageView(generic.ListView):
    template_name = "home.html"
    model = Task


class TaskView(generic.ListView):
    template_name = "task.html"
    model = Task


# Task will automatically get User_id so USER can't do it manually
class CreateTaskView(generic.CreateView):
    template_name = "add_task.html"
    model = Task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('task_view')

    def form_valid(self, form):
        form.instance.User_id = self.request.user.id
        return super().form_valid(form)


class DeteletaskView(generic.DeleteView):
    template_name = 'delete_task.html'
    model = Task
    success_url = reverse_lazy('task_view')


class EditTaskView(generic.UpdateView):
    template_name = "edit_task.html"
    model = Task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('task_view')


# Bonus Login system
class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditUserForm
    template_name = "registration/edit_user.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        user = get_object_or_404(Task, pk=self.request.user.id)
        return user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')
