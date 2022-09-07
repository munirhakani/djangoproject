from django.contrib.auth.models import User
from django.db import models
from crum import get_current_user


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        abstract = True
    
    def save(self):
        self.user = get_current_user()
        return super().save()