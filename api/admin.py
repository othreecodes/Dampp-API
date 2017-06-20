from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ['is_verified', 'is_active']
    list_display = ['username', 'full_name', 'date_joined']
    search_fields = ['full_name', 'username']
