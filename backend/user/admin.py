from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from user.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = [
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'national_id', 'birthday', 'phone_number', 'sex', 'city')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_athlete', 'is_trainer'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'slug')}),
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'national_id', 'birthday', 'phone_number', 'sex', 'city')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_athlete'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_athlete', 'is_trainer')
    list_filter = ('is_staff', 'is_active', 'is_athlete', 'sex')
    search_fields = ('email', 'first_name', 'last_name', 'slug')
    ordering = ('id', )
    readonly_fields = ('slug', 'date_joined', 'last_login', 'is_superuser', 'city')
