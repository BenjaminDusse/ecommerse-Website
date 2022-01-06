from django.db import models
from django.db.models import QuerySet

class BaseQuerySet(models.QuerySet):

    def delete(self):
        self.update(is_available=True)

class DeleteManager(models.Manager):
    def get_quryset(self) -> QuerySet:
        return BaseQuerySet(self.model).filter(is_available=False)