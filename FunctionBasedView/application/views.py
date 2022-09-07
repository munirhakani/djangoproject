from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

from application.forms import PersonForm
from application.models import Person


def PersonListView(request):
    return render(request, 'person_list.html', {'object_list': Person.objects.all()})


def PersonDetailView(request, pk):
    return render(request, 'person_detail.html', {'object': get_object_or_404(Person, pk=pk)})


def PersonCreateView(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(Person.get_object_list_url())
    return render(request, 'person_form.html', {'form': form})


def PersonUpdateView(request, pk):
    form = PersonForm(request.POST or None, instance=get_object_or_404(Person, pk=pk))
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(Person.get_object_list_url())
    return render(request, 'person_form.html', {'form': form})


def PersonDeleteView(request, pk):
    object = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        object.delete()
        return HttpResponseRedirect(Person.get_object_list_url())
    return render(request, 'person_confirm_delete.html', {'object': object})