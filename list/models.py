from django.db import models

# Create your models here.

class Order(models.Model):
	SHIRTS_CHOICES = (
			('Camiseta pré-lavada e amaciada', 'Camiseta pré-lavada e amaciada'),
			('Camiseta estonada', 'Camiseta estonada'),
			('Camiseta tingida a seco', 'Camiseta tingida a seco'),
			('Camiseta marmorizada', 'Camiseta marmorizada')
		)

	COLOURS_CHOICES = (
			('Amarelo', 'Amarelo'),
			('Azul', 'Azul'),
			('Vermelho', 'Vermelho')
		)

	SIZES_CHOICES = (
			('P', 'P'),
			('M', 'M'),
			('G', 'G'),
			('GG', 'GG')
		)

	tipo = models.CharField(max_length = 100, choices = SHIRTS_CHOICES)
	cor = models.CharField(max_length = 100, choices = COLOURS_CHOICES)
	tamanho = models.CharField(max_length = 100, choices = SIZES_CHOICES)
	quantidade = models.IntegerField(default=1)
	estoque = models.BooleanField(default=False)
	etiquetada = models.BooleanField(default=False)
	estampada = models.BooleanField(default=False)
	observacoes = models.CharField(default="", max_length = 100, blank=True, null=False)
	preco = models.DecimalField(default=0, max_digits=100, decimal_places=2, blank=True, null=False)
	pronta_entrega = models.BooleanField(default=False)

			
