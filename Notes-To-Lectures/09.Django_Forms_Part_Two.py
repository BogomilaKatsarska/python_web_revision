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


'''