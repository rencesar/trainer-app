from django.contrib import admin
from django.utils.translation import gettext as _

from athlete.models import Athlete
from utils.admin import UsersAdmin


@admin.register(Athlete)
class AthleteAdmin(UsersAdmin, admin.ModelAdmin):
    pass