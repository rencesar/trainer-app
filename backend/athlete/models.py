from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from personal.models import Personal
from utils.models import OurUser

UserModel = get_user_model()


class Athlete(OurUser, models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='athlete', null=False)
    personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)

