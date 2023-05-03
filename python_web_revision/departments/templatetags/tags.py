from django.template import Library

register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student):
    return f'Hello, my name is {student.name} and I am {student.age} years old.'


@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str(x) for x in (list(args) + list(kwargs.items())))


@register.inclusion_tag('tags/nav.html', name='app_nav', takes_context=True)
def generate_nav(url_names):
    context = {
        'url_names': url_names,
    }
    return context
