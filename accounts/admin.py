from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff',
                    'is_active', 'last_login', 'is_certified')
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',
                   'last_login', 'is_certified')
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields':
        ('email', 'first_name', 'last_name', 'password1', 'password2',
         'is_staff', 'is_active', 'is_superuser', 'is_certified')
    }), )
    search_fields = ('email', )
    ordering = ('email', )


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'email_verified', 'reputation_tier',
                    'academic_affiliation', 'academic_affiliation_verified',
                    'orcid_id', 'orcid_id_verified')
    list_filter = ('user', 'email_verified', 'reputation_tier',
                   'academic_affiliation', 'academic_affiliation_verified',
                   'orcid_id', 'orcid_id_verified')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
