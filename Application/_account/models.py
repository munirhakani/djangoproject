from django.contrib import messages
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from crum import get_current_request

from projectfiles.abstract import BaseModel
from _accounttype.models import AccountType
from .apps import AccountConfig
app_name = AccountConfig.name


class Account(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Account', help_text='Enter Account')
    accounttype = models.ForeignKey(AccountType, on_delete=models.PROTECT, verbose_name='Account Type', help_text='Select Account Type')
    parent = models.ForeignKey('Account', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Sub Account of', help_text='Select Parent Account')
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Balance')

    class Meta:
        db_table = '_account'
        ordering = ('name', )

    def __str__(self):
        return self.name
    
    def get_object_list_url():
        return reverse(app_name+':ObjectListView')

    def get_detail_url(self):
        return reverse(app_name+':ObjectDetailView', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse(app_name+':ObjectUpdateView', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse(app_name+':ObjectDeleteView', kwargs={'pk': self.pk})

    def delete(self):
        try:
            return super().delete()
        except models.ProtectedError as exception:
            messages.add_message(get_current_request(), messages.WARNING, str(exception))
            return reverse(app_name+':ObjectListView')

    def get_balance(self):
        return '{:,.2f}'.format(self.balance)


def get_account_list(request):
    return render(request, 'options.html', {'object_list': Account.objects.all()})

def get_account_list__accounttype_id(request):
    return render(request, 'options.html', {'object_list': Account.objects.filter(accounttype=request.GET.get('id'))})

def get_accounttype_pk__account_id(request):
    return HttpResponse(Account.objects.get(id=request.GET.get('id')).accounttype.pk)