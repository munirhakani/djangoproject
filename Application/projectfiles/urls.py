from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

class HomeTemplateView(TemplateView):

    def get_template_names(self):
        return ['home.html']


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='HomeTemplateView'),
    path('admin/', admin.site.urls),
    path('_accounttype/', include('_accounttype.urls', namespace='_accounttype')),
    path('_account/', include('_account.urls', namespace='_account')),
    path('_business/', include('_business.urls', namespace='_business')),
    path('_transaction/', include('_transaction.urls', namespace='_transaction')),

    # path('accounting_accounttype/', include('accounting_accounttype.urls', namespace='accounting_accounttype')),
    # path('accounting_account/', include('accounting_account.urls', namespace='accounting_account')),
    # path('application_business/', include('application_business.urls', namespace='application_business')),
    # path('application_transaction/', include('application_transaction.urls', namespace='application_transaction')),
]