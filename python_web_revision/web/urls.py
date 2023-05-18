from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from python_web_revision.web.views import delete_employee

urlpatterns = (
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
