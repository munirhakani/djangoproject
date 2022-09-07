from django import forms
from django.core.exceptions import ValidationError

from .models import Account as ModelObject

class ObjectForm(forms.ModelForm):

    class Meta:
        model = ModelObject
        fields = ('name', 'parent', 'accounttype', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs['class'] = 'select_parent'
        self.fields['parent'].empty_label = 'Click/Press <SPACE> to display list'
        self.fields['accounttype'].widget.attrs['class'] = 'select_accounttype'
        self.fields['accounttype'].empty_label = 'Click/Press <SPACE> to display list'


class ObjectFindForm(forms.Form):
    name__icontains = forms.CharField(max_length=50, label='Account Name', help_text='Enter Account Name', required=False, initial='')

    def clean(self):
        totalLength = 0
        for field in self.fields:
            totalLength += len(str(self.cleaned_data[field]))
        if totalLength == 0:
            raise ValidationError('Validation Error: At least one field is required!')
        else:
            super().clean()