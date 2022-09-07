from django.contrib import messages
from django.db import models
from django.urls import reverse
from crum import get_current_request

from projectfiles.abstract import BaseModel
from .apps import AccounttypeConfig
app_name = AccounttypeConfig.name


class SystemAccountType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='System Account Type', help_text='Enter System Account Type')

    class Meta:
        db_table = '_systemaccounttype'
        ordering = ('name', )

    def __str__(self):
        return self.name


class AccountType(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Account Type', help_text='Enter Account Type')
    systemaccounttype = models.ForeignKey(SystemAccountType, on_delete=models.PROTECT, verbose_name='System Account Type', help_text='Select System Account Type')

    class Meta:
        db_table = '_accounttype'
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