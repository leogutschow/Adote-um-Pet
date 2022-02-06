from django.urls import path

from perfil.views import teste_view

urlpatterns = [
    path('<slug:perfil>', teste_view),

]
