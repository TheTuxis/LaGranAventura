# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def book_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'book_{0}/{1}'.format(instance.id, filename)


def page_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'book_{0}/page_{1}/{2}'.format(
        instance.book.id, instance.id, filename
    )


def option_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'book_{0}/page_{1}/{2}/{3}'.format(
        instance.page.book.id, instance.page.id, instance.id, filename
    )


class Book(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    pic = models.FileField(upload_to=book_directory_path, null=True, blank=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, blank=True, null=True, related_name='books_author')
    modified_by = models.ForeignKey(User, blank=True, null=True, related_name='books_modified_by')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % (self.name,)


class Page(models.Model):
    book = models.ForeignKey(Book, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    pic = models.FileField(upload_to=page_directory_path, null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, blank=True, null=True, related_name='page_author')
    modified_by = models.ForeignKey(User, blank=True, null=True, related_name='page_modified_by')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "[%s] %s" % (self.book, self.name,)

    def get_options(self):
        return Option.objects.filter(page=self).order_by('order')


class Option(models.Model):
    page = models.ForeignKey(Page, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)
    pic = models.FileField(upload_to=option_directory_path, null=True, blank=True)
    px = models.IntegerField(null=True, blank=True)
    next_page = models.ForeignKey(Page, blank=True, null=True, related_name='option_next')
    author = models.ForeignKey(User, blank=True, null=True, related_name='option_author')
    modified_by = models.ForeignKey(User, blank=True, null=True, related_name='option_modified_by')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "[%s-%s] %s" % (self.page.book, self.page, self.name,)


class PlayerSection(models.Model):
    player = models.ForeignKey(User, blank=True, null=True)
    book = models.ForeignKey(Book, blank=True, null=True)
    actual_page = models.ForeignKey(Page, blank=True, null=True)
    px = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "[%s] %s" % (self.player, self.book)

    def get_detail(self):
        return PlayerSectionDetail.objects.filter('id')


class PlayerSectionDetail(models.Model):
    player_section = models.ForeignKey(PlayerSection, blank=True, null=True)
    actual_page = models.ForeignKey(Page, blank=True, null=True)
    option = models.ForeignKey(Option, blank=True, null=True)
    px = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "[%s] - %s" % (self.player_section.player, self.actual_page)
