from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import FormView
from Home.forms import CustomUserCreationForm, TaskForm
from django.contrib.auth import login

from Home.models import Task
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class TasksView(FormView):
    template_name = "tasks.html"
    form_class = TaskForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("Tasks")
        return render(request, self.template_name)

class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("Home")

def delete(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return HttpResponseRedirect(reverse('Tasks'))