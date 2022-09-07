from django import forms

from application.models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['name'].widget.attrs['onfocus'] = 'this.setSelectionRange(0, this.value.length)'