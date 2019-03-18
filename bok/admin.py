from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import Player


class PlayerInline(admin.StackedInline):
    model = Player
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):
    inlines = [PlayerInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)