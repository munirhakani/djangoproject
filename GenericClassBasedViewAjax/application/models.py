from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Person Name', help_text='Enter Person Name')

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name
    
    def get_object_list_url():
        return reverse('application:PersonListView')
    
    def get_detail_url(self):
        return reverse('application:PersonDetailView', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('application:PersonUpdateView', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('application:PersonDeleteView', kwargs={'pk': self.pk})