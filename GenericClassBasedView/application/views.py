from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from application.models import Person
from application.forms import PersonForm


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm

    def get_success_url(self):
        return self.model.get_object_list_url()


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm

    def get_success_url(self):
        return self.model.get_object_list_url()


class PersonDeleteView(DeleteView):
    model = Person

    def get_success_url(self):
        return self.model.get_object_list_url()