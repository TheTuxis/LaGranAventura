# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Book


@login_required()
def book_detail(request, id_book):
    books = Book.objects.filter(published=True, id=id_book)
    template = loader.get_template('main.html')
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))
