'''
0:45:23
1. Framework - platform for developing software applications
2. Django follows MTV design pattern (Model-Template-View) (DB - the presentation layer - handles business logic + gets/sets data into model/returns data to template)
3. Project and Apps
'''
from django.urls import path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('bogomila/', my_view),
)