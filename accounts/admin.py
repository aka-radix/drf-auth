from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 
        'username', 
        'age', 
        'gender', 
        'social_status', 
    ] 
    fieldsets = UserAdmin.fieldsets + ( 
        (None, {'fields': (
            'age', 
            'gender', 
            'social_status'
        )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( 
        (None, {'fields': (
            'age', 
            'gender', 
            'social_status',
            'email'
        )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)