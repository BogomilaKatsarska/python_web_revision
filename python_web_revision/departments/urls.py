from django.urls import path

from python_web_revision.departments.views import show_departments, redirect_to_first_department, show_not_found, index, \
    redirect_to_home, about

urlpatterns = (
    path('<int:department_id>/', show_departments, name='show department by id'),
    path('redirect/', redirect_to_first_department, name='redirect demo'),
    path('not-found/', show_not_found, name='not found'),
    path('', index, name='index'),
    path('', redirect_to_home, name='redirect to home'),
    path('about/', about, name='about'),
)