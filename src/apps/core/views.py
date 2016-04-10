from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


@login_required()
def main(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
