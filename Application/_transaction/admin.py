from django.contrib import admin

from .models import Transaction, TransactionNotes, TransactionAccounts


admin.site.register(Transaction)
admin.site.register(TransactionNotes)
admin.site.register(TransactionAccounts)