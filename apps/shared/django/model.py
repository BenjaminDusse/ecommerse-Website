from django.db import models

from shared.django.queryset import DeleteManager

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstractc = True

class DeleteModel(models.Model):
    is_available = models.BooleanField(default=False)

    objects = DeleteManager()

    def delete(self, **kwargs):
        self.is_available = True
        self.save()

    class Meta:
        abstract = True

