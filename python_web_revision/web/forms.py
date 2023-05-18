from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render


class PersonForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
    )
    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
        help_text='Enter your name',
    )
    comments = forms.CharField(
        widget=forms.Textarea(),
    )
    email = forms.CharField(
        widget=forms.EmailInput(),
    )


class TodoForm(forms.Form):
    text = forms.CharField(
        error_messages={
            'required': 'Todo text must be set.'
        }
    )
    is_done = forms.BooleanField(
        required=False,
    )
    profile_image = forms.ImageField(
        upload_to = 'persons',
        null = True,
        blank = True,
    )

    def clean_text(self):
        pass

    def clean_priority(self):
        raise ValidationError('pass')

    def clean_is_done(self):
        pass


def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = self.cleaned_data['name']
        return profile_image