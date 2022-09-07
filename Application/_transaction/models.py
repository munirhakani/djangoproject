from django.contrib import messages
from django.db import models
from django.urls import reverse
from crum import get_current_request

from projectfiles.abstract import BaseModel
from _notes.models import Notes
from _account.models import Account
from .apps import TransactionConfig
app_name = TransactionConfig.name


class Transaction(BaseModel):

    class Meta:
        db_table = '_transaction'
        ordering = ('-pk', )

    def __str__(self):
        return 'Transaction # ' + str(self.pk)

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


class TransactionNotes(Notes):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)

    class Meta:
        db_table = '_transactionnotes'

    def __str__(self):
        return 'Transaction # ' + str(self.transaction.pk) + ', ' + self.notes


class TransactionAccounts(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name='Account', help_text='Select Account')
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Amount')

    class Meta:
        db_table = '_transactionaccounts'

    def __str__(self):
        return 'Transaction # ' + str(self.transaction.pk) + ', ' + self.account.name