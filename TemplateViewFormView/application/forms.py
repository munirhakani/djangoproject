from django import forms
from django.core.exceptions import ValidationError

from application.models import Person


class PersonRawForm(forms.Form):
    name = forms.CharField(max_length=50, label='Person Name', help_text='Enter Person Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['name'].widget.attrs['onfocus'] = 'this.setSelectionRange(0, this.value.length)'

    def clean(self):
        if Person.objects.filter(name=self.cleaned_data['name']).exists():
            raise ValidationError('Validation Error: Duplication Error')
        else:
            super().clean()


class DeleteForm(forms.Form):
    isOk2Delete = forms.BooleanField(widget=forms.HiddenInput(), required=False)