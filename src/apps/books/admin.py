# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Book, Page, Option, PlayerSection, PlayerSectionDetail


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'author', 'modified_by', 'date_created',
        'date_update', 'published'
    )
    list_filter = ('published',)
    search_fields = ('name', 'description',)
admin.site.register(Book, BookAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'book', 'author', 'modified_by', 'date_created',
        'date_update', 'page_number'
    )
    list_filter = ('book',)
    search_fields = ('name', 'description',)
admin.site.register(Page, PageAdmin)


class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'page', 'name', 'order', 'px', 'next_page',
    )
    list_filter = ('page',)
    search_fields = ('name', 'description',)
admin.site.register(Option, OptionAdmin)


class PlayerSectionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'player', 'book', 'actual_page', 'px'
    )
    list_filter = ('book', 'player',)
    search_fields = ('book__name', 'player__first_name', 'player__last_name',)
admin.site.register(PlayerSection, PlayerSectionAdmin)


class PlayerSectionDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'player_section', 'actual_page', 'option'
    )
    list_filter = ('player_section',)
    search_fields = ('player_section__book__name', 'player__last_name',)
admin.site.register(PlayerSectionDetail, PlayerSectionDetailAdmin)
