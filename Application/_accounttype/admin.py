from django.contrib import admin

from .models import SystemAccountType, AccountType


admin.site.register(SystemAccountType)
admin.site.register(AccountType)