from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Eod(models.Model):
    """
    Modelo que representa una Eod.
    """
    name = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")
    level = models.CharField(max_length=200)
    code = models.CharField(max_length=100, help_text="Ingrese una breve descripción del libro")
    
    eod_father = models.ForeignKey ('self', related_name="father", null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        """
        String que representa al objeto Eod
        """
        return self.name


    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Eod
        """
        return reverse('eo_detail', args=[str(self.id)])