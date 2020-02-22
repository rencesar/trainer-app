from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils.models import OurUser

UserModel = get_user_model()


class Personal(OurUser, models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='personal', null=False)

