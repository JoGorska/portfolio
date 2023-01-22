from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
