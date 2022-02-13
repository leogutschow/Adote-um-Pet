from django.urls import path
from .views import HomePesquisa, HomeView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pesquisa', HomePesquisa.as_view(), name='pesquisa')
]
