from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required()
def main(request):
    return HttpResponse("Hello, world. You're at the polls index.")
