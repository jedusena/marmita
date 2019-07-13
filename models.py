from django.db import models
from django.conf import settings
from django.utils import timezone

class Marmita(models.Model):
	Nome = models.CharField(max_length=200)
	Descrição = models.TextField()
	Ingredientes = models.TextField()
	Quantidade_estoque = models.IntegerField()
	Ulr_image = models.CharField(max_length=200)
	Preco = models.DecimalField(max_digits=5, decimal_places=2)
	Porcentagem = models.DecimalField(max_digits=5, decimal_places=2)



