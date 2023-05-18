'''
- We use tuple of validators for forms:

class TodoForm(forms.Form):
    text = forms.CharField(
        validators = (
            validate_text,
        ),
    )
    is_done = forms.BooleanField(
        required = False,
    )

def clean(self):
    return super().clean()

def clean_text():
    use for:
    1. Transform data into desired format/form
    2. Validation

def clean_priority():
    pass

def clean_is_done():
    pass


if form.is_valid():
    model = form.instance
    model.full_clean() --> method of models!

def clean_assignee(self):
    assignee = self.cleaned_data['assignee']
    if assignee.todo_set.count() >= 3:
        raise ValidationError(f'{assignee} already has max todos assigned.')
    return assignee

EXCEPTIONS - we use 'code':

def validate_text(value):
    if '_' in value:
        raise ValidationError(
            message='_ is invalid character for text.',
            code='invalid',
        )

MEDIA FILES - pictures, music, audios, videos and documents.
Computer programs or applications can read and work with a digital file after it is encoded during the saving process.
Pillow (Python Imaging Library) - it adds support for opening, manipulating and saving many different image file formats
0.)pip install pillow
also don't forget:
1.)
else:
    form = PersonCreateForm(request.POST, request.FILES)
2.)
add encryption type in the template:
<form method='post' action='{% url "create person" %}' enctype="multipart/form-data">
    {{form}}
    {% csrf_token %}
</form>
3.)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
or
MEDIA_ROOT = BASEDIR / 'media_files'
MEDIA_URL = '/media/'
4.) additional config in our urls = ()
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<img width="50" src="/media/{{person.profile_image}}/>
'''
