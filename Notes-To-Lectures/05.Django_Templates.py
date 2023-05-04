'''
2:57
SSR = Server-side rendering (HTTP response returns the needed template)
CSR = Client-side rendering (React, Angular, Vue..)

DTL and Jinja2

1.{{Variables}}

2.Filters - modifies variables for display
    - use a pipe '|' to apply a filter to a variable
    - some filters take arguments. use colon ':' to mark arguments
    - custom filters: in your application create a templatetags module
    with your custom filter file

3.{%Tags%}
{% if ...%}
{% elif ...%}
{% endif ...%}

{% empty %} --> we use it if there is nothing in the list
{% csrf_token %}
    - url tag
    custom tags
    - simple tag - processes the data and returns a string
    - inclusion tag - processes the data and returns a rendered template

4.{# Comments #} --> CTRL + /

5. Template Inheritance - block, endblock, extends

6. Static Files in Django - CSS, JavaScript, etc.

7. BOOTSTRAP - load CSS and JS in base template
'''

