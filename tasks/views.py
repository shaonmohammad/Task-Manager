from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Task, TaskImage
from . forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.base import RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user.id
        queryset = Task.objects.filter(user=user)

        # Search by title
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)

        # Filter by creation date
        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            queryset = queryset.filter(created_at__date=creation_date)

        # Filter by due date
        due_date = self.request.GET.get('due_date')
        if due_date:
            queryset = queryset.filter(due_date__date=due_date)

        # Filter by priority
        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)

        is_complete = self.request.GET.get('is_complete')
        if is_complete:
            # Convert to lowercase to handle case-insensitivity
            is_complete = is_complete.lower()
            if is_complete == "true":
                queryset = queryset.filter(is_complete=True)
            elif is_complete == "false":
                queryset = queryset.filter(is_complete=False)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_details.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        task_images = task.images.all()
        context['task_images'] = task_images
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        p = form.save()
        images = self.request.FILES.getlist("images")
        for img in images:
            TaskImage.objects.create(task=p, images=img)
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        p = form.save()
        images = self.request.FILES.getlist("images")
        for img in images:
            TaskImage.objects.create(task=p, images=img)
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirmation_delete.html'
    success_url = reverse_lazy('task_list')


class TaskImageDeleteView(DeleteView):
    model = TaskImage
    template_name = 'task_image_confirm_delete.html'
    context_object_name = 'tasks'

    def get_success_url(self):
        # Get the task associated with the deleted image
        task = self.object.task
        # Redirect to the 'task_details' page for the task
        return reverse_lazy('task_details', kwargs={'pk': task.id})
