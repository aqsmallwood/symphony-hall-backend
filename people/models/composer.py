from django.db import models


class Composer(models.Model):
    given_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.family_name}, {self.given_name}'

    @property
    def full_name(self):
        return f'{self.given_name} {self.family_name}'
