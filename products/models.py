from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    # Use a CharField or URLField to store image paths or URLs
    image_url = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name

