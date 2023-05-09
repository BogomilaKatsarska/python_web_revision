from django.urls import path

from python_web_revision.web.views import delete_employee

urlpatterns = (
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
)