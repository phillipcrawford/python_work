from django.db import models

# Create your models here.
class Blog(models.Model):
    """One person's blog."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class BlogPost(models.Model):
    """Individual psot."""
    blog = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.title) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"