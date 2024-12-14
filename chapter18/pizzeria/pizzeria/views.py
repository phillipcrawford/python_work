from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzeria/index.html')

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza and all its toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria/pizza.html', context)