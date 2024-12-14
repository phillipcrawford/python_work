"""Define URL patterns for pizzeria."""

from django.urls import path

from . import views

app_name = 'pizzeria'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topic.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
