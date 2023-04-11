from django.urls import path

from python_web_revision.departments.views import show_departments

urlpatterns = (
    path('<int:department_id>/', show_departments),
)