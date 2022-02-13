from django.contrib import admin
from .models import Animal, Especie, Raca
# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'local', 'doador', 'especie', )

admin.site.register(Animal, AnimalAdmin)

admin.site.register(Especie)

admin.site.register(Raca)