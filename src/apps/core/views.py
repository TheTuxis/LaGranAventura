# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from ..books.models import Book


@login_required()
def main(request):
    books_list = Book.objects.filter(published=True)
    template = loader.get_template('main.html')
    context = {
        'books_list': books_list,
    }
    return HttpResponse(template.render(context, request))


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        email = request.POST.get('email', None)
        if form.is_valid() and email:
            new_user = form.save()
            new_user.is_active = False
            new_user.email = email
            new_user.save()
            return main(request)
    template = loader.get_template('registration/signup.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
