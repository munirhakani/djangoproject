from django import forms
from django.core.exceptions import ValidationError

from .models import AccountType as ModelObject


class ObjectForm(forms.ModelForm):

    class Meta:
        model = ModelObject
        fields = ('name', 'systemaccounttype', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['systemaccounttype'].empty_label = 'Click/Press <SPACE> to display list'


class ObjectFindForm(forms.Form):
    name__icontains = forms.CharField(max_length=50, label='AccountType Name', help_text='Enter AccountType Name', required=False, initial='')

    def clean(self):
        totalLength = 0
        for field in self.fields:
            totalLength += len(str(self.cleaned_data[field]))
        if totalLength == 0:
            raise ValidationError('Validation Error: At least one field is required!')
        else:
            super().clean()