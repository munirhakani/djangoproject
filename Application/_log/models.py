from django.db import models
from projectfiles.choices import action_choice


class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=50)
    modelpk = models.BigIntegerField()
    action = models.CharField(max_length=1, choices=action_choice, default='C')

    class Meta:
        db_table = '_log'


class DataBeforeUpdate(models.Model):
    model = models.CharField(max_length=50)
    modelpk = models.BigIntegerField()
    databeforeupdate = models.JSONField()

    class Meta:
        db_table = '_databeforeupdate'