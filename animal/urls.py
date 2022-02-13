from django.urls import path
from animal.views import AnimalDetalhe

app_name = 'pet'

urlpatterns = [
    path('detalhe/<slug:slug>', AnimalDetalhe.as_view(), name='detalhe')
]