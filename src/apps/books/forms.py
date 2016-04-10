# -*- coding: utf-8 -*-
from django import forms
from .models import Book, Page, Option, PlayerSection, PlayerSectionDetail


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'pic', 'published')


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('book', 'name', 'description', 'pic', 'page_number')


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = (
            'page', 'name', 'description', 'order', 'pic', 'px', 'next_page'
        )


class PlayerSectionForm(forms.ModelForm):
    class Meta:
        model = PlayerSection
        fields = ('player', 'book', 'actual_page', 'px')


class PlayerSectionDetailForm(forms.ModelForm):
    class Meta:
        model = PlayerSectionDetail
        fields = (
            'player_section', 'actual_page', 'option', 'px'
        )
