# -*- coding: utf-8 -*-
from django import forms
from apps.core.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'avatar')
