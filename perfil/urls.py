from django.urls import path

from perfil.views import teste_view

app_name = 'perfil'

urlpatterns = [
    path('<str:nome>', teste_view.as_view(), name='detalhe'),

]
