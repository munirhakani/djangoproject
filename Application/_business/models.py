from django.contrib import messages
from django.db import models
from django.urls import reverse
from crum import get_current_request

from projectfiles.abstract import BaseModel
from .apps import BusinessConfig
app_name = BusinessConfig.name


class Business(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Business', help_text='Enter Business')
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Balance')

    class Meta:
        db_table = '_business'
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