from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _


UserModel = get_user_model()


class UserInline(admin.StackedInline):
    fieldsets = [
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
    add_fieldsets = (None, {
        'fields': ('email', 'password1', 'password2'),
    })
    form = UserChangeForm
    add_form = UserCreationForm
    model = UserModel
    readonly_fields = ('last_login', 'date_joined')
    extra = 1

    def get_fieldsets(self, request, obj=None):
        if not obj:
            self.fieldsets[0] = self.add_fieldsets
            return self.fieldsets
        return super().get_fieldsets(request, obj)

    def get_formset(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        if obj is None:
            self.form = self.add_form
        return super().get_formset(request, obj, **kwargs)


class UsersAdmin:
    inlines = (UserInline, )
    list_display = ('get_email', 'get_first_name', 'get_last_name', 'get_is_active')
    list_filter = ('user__is_staff', 'user__is_superuser', 'user__is_active')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')

    def get_queryset(self, request):
        return super(UsersAdmin, self).get_queryset(request).select_related('user')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First name'
    get_first_name.admin_order_field = 'user__last_name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last name'
    get_last_name.admin_order_field = 'user__last_name'

    def get_is_active(self, obj):
        return obj.user.is_active
    get_is_active.short_description = 'Is active'
    get_is_active.admin_order_field = 'user__is_active'


admin.site.unregister(Group)
