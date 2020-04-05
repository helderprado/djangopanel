from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = [
			'tipo',
			'cor',
			'tamanho',
			'quantidade',
			'observacoes',
			'preco',
			'pronta_entrega'
		]