from django.urls import path

from python_web_revision.departments.views import show_departments, redirect_to_first_department, show_not_found

urlpatterns = (
    path('<int:department_id>/', show_departments, name='show department by id'),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
    path('not-found/', show_not_found, name='not found'),
)