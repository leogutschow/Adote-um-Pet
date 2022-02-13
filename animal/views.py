from django.shortcuts import render
from django.views.generic import DetailView
from .models import Animal

# Create your views here.

class AnimalDetalhe(DetailView):
    template_name = 'animal/detalhe.html'
    model = Animal

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        animal = self.get_object()

        detalhes = Animal.objects.get(slug=animal.slug)

        contexto['animal'] = animal

        return contexto



