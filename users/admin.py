from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_teacher', 'is_student']


admin.site.register(User, UserAdmin)
