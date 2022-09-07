from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView

from projectfiles.settings import PAGINATE_BY
from projectfiles.library import SafePaginator
from projectfiles.library import SuccessUrlMixin

from .apps import AccountConfig
app_name = AccountConfig.name
from .forms import ObjectForm
from .forms import ObjectFindForm
from .models import Account as ModelObject


class ObjectTemplateView(TemplateView):
    template_name = app_name + '/object_template.html'


class ObjectListView(ListView):
    model = ModelObject
    paginator_class = SafePaginator
    paginate_by = PAGINATE_BY
    template_name = app_name + '/object_list.html'

    def get_queryset(self):
        find = self.request.GET.get('find')
        if find:
            get_queryset = super().get_queryset().filter(**eval(find))
        else:
            get_queryset = super().get_queryset()

        if self.request.GET.get('sortby'):
            return get_queryset.order_by(self.request.GET.get('sortby', 'name'))
        else:
            return get_queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['find'] = self.request.GET.get('find', '')
        context['sortby'] = self.request.GET.get('sortby', 'name')
        return context


class ObjectDetailView(DetailView):
    model = ModelObject
    template_name = app_name + '/object_detail.html'


class ObjectFindView(FormView):
    model = ModelObject
    form_class = ObjectFindForm
    template_name = app_name + '/object_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['find'] = True
        return context
    
    def form_valid(self, form):
        self.success_url = self.model.get_object_list_url() \
            + '?page=' + '1' \
            + '&sortby=' + self.request.POST.get('sortby') \
            + '&find=' + str(form.cleaned_data)
        return super().form_valid(form)

    
class ObjectCreateView(SuccessUrlMixin, CreateView):
    model = ModelObject
    form_class = ObjectForm
    template_name = app_name + '/object_form.html'


class ObjectUpdateView(SuccessUrlMixin, UpdateView):
    model = ModelObject
    form_class = ObjectForm
    template_name = app_name + '/object_form.html'


class ObjectDeleteView(SuccessUrlMixin, DeleteView):
    model = ModelObject
    template_name = app_name + '/object_delete.html'