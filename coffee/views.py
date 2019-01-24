from django.shortcuts import render

from django.views.generic import TemplateView

from . import models

class HomeView(TemplateView):
    template_name = 'coffees/home.html'

    def get_context_data(self, **kwargs):
        good_coffees = models.Coffee.objects.filter(origin='Methodical')

        context = {
            'coffees' : good_coffees
        }