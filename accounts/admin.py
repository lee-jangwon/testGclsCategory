from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "username",
        "email",
    ]


admin.site.register(User, CustomUserAdmin)
