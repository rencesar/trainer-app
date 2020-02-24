from django.db import models
from django.utils.translation import gettext as _

from personal.models import Personal


class Athlete(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return _('Atleta: %s' % self.user.first_name)

