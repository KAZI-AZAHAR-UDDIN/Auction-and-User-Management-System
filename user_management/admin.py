from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User

class UserAdmin(DefaultUserAdmin):
    model = User

admin.site.register(User, UserAdmin)
