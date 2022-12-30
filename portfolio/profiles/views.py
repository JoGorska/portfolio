from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class ProfileView(TemplateView):
    template_name = 'profile/profile.html'