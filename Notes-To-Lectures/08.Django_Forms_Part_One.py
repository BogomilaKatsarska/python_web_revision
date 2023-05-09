'''
40:00
GET and POST are the only HTTP methods to use when dealing with forms
<form action='/your-name/' method='post'></form>

from django import forms

class NameForm(forms.Form):
    your_name=forms.CharField(
        label='Your name',
        max_length=50,
    )

def index(request):
    context = {
        'form':NameForm,
    }
    return render(request, 'index.html', context)

'''