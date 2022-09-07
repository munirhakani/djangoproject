from django.contrib import messages
from django.db import models
from django.urls import reverse
from crum import get_current_request

from projectfiles.abstract import BaseModel
from .apps import NotesConfig
app_name = NotesConfig.name


class Notes(BaseModel):
    notes = models.CharField(max_length=100, unique=True, verbose_name='Notes', help_text='Enter Notes')

    class Meta:
        db_table = '_notes'
        ordering = ('notes', )

    def __str__(self):
        return self.notes
    
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