from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from application.forms import PersonRawForm
from application.forms import DeleteForm
from application.models import Person


class PersonListView(TemplateView):
    template_name = 'person_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Person.objects.all()
        return context_data


class PersonDetailView(TemplateView):
    template_name = 'person_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object'] = Person.objects.get(pk=self.kwargs['pk'])
        return context_data


class PersonCreateView(FormView):
    template_name = 'person_form.html'
    form_class = PersonRawForm
    success_url = '../'

    def form_valid(self, form):
        Person.objects.create(**form.cleaned_data)
        return super().form_valid(form)


class PersonUpdateView(FormView):
    template_name = 'person_form.html'
    form_class = PersonRawForm
    success_url = '../../'

    def get_initial(self):
        object = Person.objects.get(pk=self.kwargs['pk'])
        initial = super().get_initial()
        initial['name'] = object.name
        return initial

    def form_valid(self, form):
        object = Person.objects.get(pk=self.kwargs['pk'])
        object.name = form.cleaned_data['name']
        object.save()
        return super().form_valid(form)


class PersonDeleteView(FormView):
    template_name = 'person_confirm_delete.html'
    form_class = DeleteForm
    success_url = '../../'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object'] = Person.objects.get(pk=self.kwargs['pk'])
        return context_data

    def form_valid(self, form):
        Person.objects.filter(pk=self.kwargs['pk']).delete()
        return super().form_valid(form)