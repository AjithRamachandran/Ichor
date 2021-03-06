from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group

from core.models import User
from profiles.models import Profile
from blood_banks.models import BloodBank

class UserAdmin(BaseUserAdmin):
    ordering = ('id',)
    list_display = ('email',)
    fieldsets = (
        (None, {
            'fields': ('email','password',)
        }),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser',)
        }),
        (_('Account information'), {
            'fields': ('is_active', 'last_login',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(BloodBank)
admin.site.unregister(Group)
