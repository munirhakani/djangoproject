# Generated by Django 4.0.5 on 2022-07-26 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemAccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter System Account Type', max_length=50, unique=True, verbose_name='System Account Type')),
            ],
            options={
                'db_table': '_systemaccounttype',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Enter Account Type', max_length=50, unique=True, verbose_name='Account Type')),
                ('systemaccounttype', models.ForeignKey(help_text='Select System Account Type', on_delete=django.db.models.deletion.PROTECT, to='_accounttype.systemaccounttype', verbose_name='System Account Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_accounttype',
                'ordering': ('name',),
            },
        ),
    ]
