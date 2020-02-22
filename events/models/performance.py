from django.db import models

from music.models import Work
from people.models import Performer

class Performance(models.Model):
    performed_at = models.DateField()
    performers = models.ManyToManyField(Performer)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.performed_at} {self.work}'
