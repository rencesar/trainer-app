from django.utils.translation import gettext as _


class UsersAdmin:
    fieldsets = (
        (None, {'fields': ('user__email', 'user__password')}),
        (_('Personal info'), {'fields': ('user__first_name', 'user__last_name',)}),
        (_('Permissions'), {
            'fields': ('user__is_active', 'user__is_staff', 'user__is_superuser', ),
        }),
        (_('Important dates'), {'fields': ('user__last_login', 'user__date_joined')}),
    )
    list_display = ('cpf', 'get_email', 'get_first_name', 'get_last_name', 'get_is_active')
    list_filter = ('user__is_staff', 'user__is_superuser', 'user__is_active')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    readonly_fields = ('cpf', 'user__password', )

    def get_queryset(self, request):
        return super(UsersAdmin, self).get_queryset(request).select_related('user')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_first_name(self, obj):
        return obj.user.last_name
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
