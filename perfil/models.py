from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Sobrenome')
    email = models.EmailField(verbose_name='E-mail', blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(verbose_name='Slug')

    def save(self, *args, **kwargs):
       super(Perfil, self).save(*args, **kwargs) # Call the real save() method
       if not self.slug:
           self.slug = slugify(self.username)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'