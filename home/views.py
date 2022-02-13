from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from animal.models import Animal

# Create your views here.
class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'animais'
    model = Animal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        animais = Animal.objects.all()

        context['animais'] = animais

        return context

