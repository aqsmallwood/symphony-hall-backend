from django.contrib.auth.models import User
from django.db import models

from people.models import Composer


class Work(models.Model):
    name = models.CharField(max_length=300)
    composers = models.ManyToManyField(Composer)

    def __str__(self):
        return self.name


class HeardWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.work.__str__()

    class Meta:
        unique_together = [['work', 'user']]


class SeenWork(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.work.__str__()

    class Meta:
        unique_together = [['work', 'user']]
