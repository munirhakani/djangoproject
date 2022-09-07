from django import forms
from django.core.exceptions import ValidationError

from .models import Business as ModelObject


class ObjectForm(forms.ModelForm):

    class Meta:
        model = ModelObject
        fields = ('name', )


class ObjectFindForm(forms.Form):
    name__icontains = forms.CharField(max_length=50, label='Business Name', help_text='Enter Business Name', required=False, initial='')

    def clean(self):
        totalLength = 0
        for field in self.fields:
            totalLength += len(str(self.cleaned_data[field]))
        if totalLength == 0:
            raise ValidationError('Validation Error: At least one field is required!')
        else:
            super().clean()