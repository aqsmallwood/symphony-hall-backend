from django.db import models

from people.models import Composer


class Work(models.Model):
    name = models.CharField(max_length=300)
    composers = models.ManyToManyField(Composer)

    def __str__(self):
        return self.name
