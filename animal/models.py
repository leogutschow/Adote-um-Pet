from django.db import models
from perfil.models import Perfil
from django.utils.text import slugify

# Create your models here.
class Especie(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome
    

class Raca(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    especie = models.OneToOneField(to=Especie, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    idade = models.IntegerField()
    local = models.CharField(max_length=255)
    doador = models.OneToOneField(to=Perfil, on_delete=models.CASCADE, blank=False, null=False)
    especie = models.OneToOneField(to=Especie, on_delete=models.DO_NOTHING, blank=False, null=False)
    raca = models.OneToOneField(to=Raca, on_delete=models.DO_NOTHING, blank=True, null=True)
    descricao = models.TextField()
    slug = models.SlugField(verbose_name='Slug', blank=True, null=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save()
        