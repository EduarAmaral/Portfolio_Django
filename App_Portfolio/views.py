from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class PortfolioView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tecnologias'] = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'SQL']
        return context