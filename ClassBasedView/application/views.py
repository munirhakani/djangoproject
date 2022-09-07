from django.views import View
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

from application.forms import PersonForm
from application.models import Person


class PersonListView(View):

    def get(self, request):
        return render(request, 'person_list.html', {'object_list': Person.objects.all()})


class PersonDetailView(View):

    def get(self, request, pk):
        return render(request, 'person_detail.html', {'object': get_object_or_404(Person, pk=pk)})


class PersonCreateView(View):
    template_name = 'person_form.html'
    form_class = PersonForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(Person.get_object_list_url())
        else:
            return render(request, self.template_name, {'form': form})


class PersonUpdateView(View):
    template_name = 'person_form.html'
    form_class = PersonForm

    def get(self, request, pk):
        form = self.form_class(instance=get_object_or_404(Person, pk=pk))
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        form = self.form_class(request.POST, instance=get_object_or_404(Person, pk=pk))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(Person.get_object_list_url())
        else:
            return render(request, self.template_name, {'form': form})


class PersonDeleteView(View):

    def get(self, request, pk):
        return render(request, 'person_confirm_delete.html', {'object': get_object_or_404(Person, pk=pk)})
    
    def post(self, request, pk):
        object = get_object_or_404(Person, pk=pk)
        object.delete()
        return HttpResponseRedirect(Person.get_object_list_url())