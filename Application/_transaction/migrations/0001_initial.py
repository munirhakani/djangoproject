# Generated by Django 4.0.5 on 2022-07-26 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('_account', '0001_initial'),
        ('_notes', '0002_alter_notes_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_transaction',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='TransactionNotes',
            fields=[
                ('notes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='_notes.notes')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='_transaction.transaction')),
            ],
            options={
                'db_table': '_transactionnotes',
            },
            bases=('_notes.notes',),
        ),
        migrations.CreateModel(
            name='TransactionAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=14, verbose_name='Amount')),
                ('account', models.ForeignKey(help_text='Select Account', on_delete=django.db.models.deletion.PROTECT, to='_account.account', verbose_name='Account')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='_transaction.transaction')),
            ],
            options={
                'db_table': '_transactionaccounts',
            },
        ),
    ]
