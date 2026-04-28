from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    TIPO_CHOICES = [
        ('capa_mole', 'Capa Mole'),
        ('capa_dura', 'Capa Dura'),
        ('bolso', 'Livro de Bolso'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=1)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='outro')
    ano = models.IntegerField(null=True, blank=True)
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo