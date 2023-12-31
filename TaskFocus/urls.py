"""
URL configuration for TaskFocus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Home.views import HomeView, MusicView, RegisterView, TasksView, delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="Home"),
    path('tasks/', TasksView.as_view(), name="Tasks"),
    path('register/', RegisterView.as_view(), name="Register"),
    path('accounts/', include("django.contrib.auth.urls"), name="Accounts"),
    path('delete/<int:id>', delete, name='delete'),
    path('music/', MusicView.as_view(), name="Music")
    ]
