from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ['name', 'accounttype', 'get_parent', 'get_balance', 'created', 'updated', 'user']

    def get_parent(self, object):
        return object.parent if object.parent else ''
    get_parent.short_description = 'Sub Account of'

    # def get_balance(self, object):
    #     return '{:,.2f}'.format(object.balance)
        
admin.site.register(Account, AccountAdmin)