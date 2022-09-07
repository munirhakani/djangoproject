from django.contrib.auth.models import User
from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True

"""
Log Management
"""
from projectfiles.choices import action_choice
class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=50)
    modelpk = models.BigIntegerField()
    action = models.CharField(max_length=1, choices=action_choice, default='C')


class DataBeforeUpdate(models.Model):
    model = models.CharField(max_length=50)
    modelpk = models.BigIntegerField()
    databeforeupdate = models.JSONField()


"""
Address Book
"""
# class Person(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Person Full Name', help_text='Enter Person Full Name')
#     isactive = models.BooleanField(default=True)
############################################
#     django.contrib.auth.models import User
############################################


class Contact(models.Model):
    contact = models.CharField(max_length=10, unique=True, verbose_name='Contact Number', help_text='Enter Contact Number')
    isactive = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Address(models.Model):
    address = models.CharField(max_length=100, unique=True, verbose_name='Address', help_text='Enter Address')
    zip = models.CharField(max_length=5)
    isactive = models.BooleanField(default=True)


class Email(models.Model):
    email = models.CharField(max_length=50, unique=True, verbose_name='Email Address', help_text='Enter Email Address')
    isactive = models.BooleanField(default=True)



"""
Accounting
"""
class SystemAccountType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='System Account Type', help_text='Enter System Account Type')

class AccountType(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Account Type', help_text='Enter Account Type')
    systemaccounttype = models.ForeignKey(SystemAccountType, on_delete=models.PROTECT, verbose_name='System Account Type', help_text='Select System Account Type')

class Account(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Account', help_text='Enter Account')
    accounttype = models.ForeignKey(AccountType, on_delete=models.PROTECT, verbose_name='Account Type', help_text='Select Account Type')
    parent = models.ForeignKey('Account', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Sub Account of', help_text='Select Parent Account')
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Balance')


class Business(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Business', help_text='Enter Business')
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Balance')


class Notes(BaseModel):
    notes = models.CharField(max_length=100, unique=True, verbose_name='Notes', help_text='Enter Notes')


class Transaction(BaseModel):
    pass

class TransactionNotes(Notes):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)

class TransactionAccounts(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name='Account', help_text='Select Account')
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name='Amount')


# check_number = models.IntegerField(unique=True)
# reference = models.CharField(max_length=20)
# notes = models.TextField(max_length=300, null=True, blank=True)