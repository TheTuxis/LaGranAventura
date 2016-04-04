# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user',
    )
    search_fields = ('user__fisrt_name', 'user__last_name',)
admin.site.register(UserProfile, UserProfileAdmin)
