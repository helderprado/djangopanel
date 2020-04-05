from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Order
from .forms import OrderForm

# Create your views here.

def home_view(request, *args, **kwargs):

	form = OrderForm(request.POST or None)

	if form.is_valid():
		form.save()
		all_items = Order.objects.all
		messages.success(request, ("A ordem foi adicionada com sucesso!"))

	else:
		all_items = Order.objects.all

	context = {
		'form': form,
		'all_items': all_items
		}

	return render(request, 'home.html', context)

def estoque(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.estoque = False
	item.save()
	return redirect('home')

def etiquetada(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.etiquetada = False
	item.save()
	return redirect('home')

def estampada(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.estampada = False
	item.save()
	return redirect('home')

def verificar_estoque(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.estoque = True
	item.save()
	return redirect('home')

def verificar_etiquetada(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.etiquetada = True
	item.save()
	return redirect('home')

def verificar_estampada(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.estampada = True
	item.save()
	return redirect('home')

def delete(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.delete()
	return redirect('home')

def pronta_entrega(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.pronta_entrega = False
	item.save()
	return redirect('home')

def verificar_pronta_entrega(request, list_id):
	item = Order.objects.get(pk=list_id)
	item.pronta_entrega = True
	item.save()
	return redirect('home')

def edit(request, list_id):

	if request.method == "POST":
		item = Order.objects.get(pk=list_id)

		form = OrderForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ("A sua ordem foi editada."))
			return redirect('home')


	else:
		item = Order.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})

def observacoes(request, list_id):

	if request.method == "POST":
		item = Order.objects.get(pk=list_id)

		form = OrderForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ("A sua observação foi adicionada."))
			return redirect('home')


	else:
		item = Order.objects.get(pk=list_id)
		return render(request, 'observacoes.html', {'item': item})


