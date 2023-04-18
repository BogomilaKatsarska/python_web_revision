'''
1. Slugs - unique
2. Dynamic URLs
    path('department/<int:department_id>/', views.show_department_by_id)
    include converter type (e.g.: int:)
3. Django Shortcut Functions (from django.shortcuts import render, redirect..)
- render(request, template_name='departments/departments_by_id'
4. Views returning errors
5. Environmental Variables:
SECRET_KEY = os.environ.get('SECRET_KEY', 'purple unicorn')
'''