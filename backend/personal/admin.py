from django.contrib import admin
from django.utils.translation import gettext as _

from personal.models import Personal
from utils.admin import UsersAdmin


@admin.register(Personal)
class PersonalAdmin(UsersAdmin, admin.ModelAdmin):
    pass
