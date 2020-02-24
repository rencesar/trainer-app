from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


class Personal(models.Model):

    def __str__(self):
        return _('Personal: %s' % self.user.first_name)

