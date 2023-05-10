from django import forms


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