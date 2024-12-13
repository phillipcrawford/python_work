from django.db import models

class Pizza(models.Model):
    """A Pizza the user is ordering"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class Topping(models.Model):
    """A Topping to be put on the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.name[:50]}"
