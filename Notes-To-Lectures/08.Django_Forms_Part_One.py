'''
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
        'form':NameForm(),
    }
    return render(request, 'index.html', context)

def add_new_name(request):
    name = None
    if request.method == 'GET':
        form = NameForm()
    else:
    # request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid()
        name = form.cleaned_data['your_name']
        context = {
            'form': form,
            'name': name,
        }

    return render(request, 'index.html', context)


is_valid:
1. validates the form, returns 'True/False'
2. fills 'cleaned_data'


form.as_div
form.as_p
form.as_table
form.as_ul


{% csrf_token %}

choice_field = forms.ChoiceField(choices=CHOICES)
select - dropdown
checkbox
radio button - select only one


ModelForm Class:

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        #fields = ['first_name', 'last_name']
        #exclude = ('pets',)


    ...
    form = PersonCreateForm(request.POST)
    if form.is_valid():
        # Person.objects.create(
        #     **form.cleaned_data
        # )
        form.save()
'''