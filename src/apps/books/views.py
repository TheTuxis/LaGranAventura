# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Book, Page
from .forms import PlayerSectionDetailForm


@login_required()
def book_detail(request, id_book):
    book = Book.objects.get(published=True, id=id_book)
    template = loader.get_template('books/books_detail.html')
    context = {
        'book': book,
    }
    return HttpResponse(template.render(context, request))


@login_required()
def page_detail(request, id_book, id_page):
    book = Book.objects.get(published=True, id=id_book)
    page = Page.objects.get(id=id_page)
    form = PlayerSectionDetailForm()
    template = loader.get_template('books/page_detail.html')
    context = {
        'book': book,
        'page': page,
        'form': form
    }
    return HttpResponse(template.render(context, request))
