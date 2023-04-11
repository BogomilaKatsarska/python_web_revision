'''
1. Framework - platform for developing software applications
2. Django follows MTV design pattern (Model-Template-View) (DB - the presentation layer - handles business logic + gets/sets data into model/returns data to template)
3. Project and Apps
    python manage.py startapp tasks
- include the app to the project's INSTALLED_APPS:
    1. Django Apps
    2. Third-Party Apps
    3. Application Apps
4. Setting up a DB
- hide credentials with environment variables
- use adapter/driver/connector  to connect to PostgreSQL - Psycopg2
    pip install psycopg2
5. Django Models
    python manage.py makemigrations
    python manage.py migrate
6. Django Admin Site
    url/admin
    python manage.py createsuperuser
7. Django Views - FBV and CBV

SHIFT + F6 ---> Rename (e.g.:a function and all its usages)

8. Creating a simple design - Template
{{title}}
{%for task in tasks%}
<li>{{task.name}}</li>
{%endfor%}
'''
from django import http
from django.contrib import admin
from django.db import models
from django.shortcuts import render
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('bogomila/', include('django101.tasks.urls')),
)


#Maps to a DB Table
class Task(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
    )
    description = models.TextField()
    priority = models.IntegerField()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Tuple below
    list_display = ('id', 'name', 'priority')


def index(request):
    return http.HttpResponse('It works')


def get_all_tasks(request):
    all_tasks = Task.objects.order_by('id').all()
    result = ', '.join(f'{t.name} ({t.id})' for t in all_tasks)
    return http.HttpResponse(result)


def index2(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)