from django.db import models
from ecommerce.settings import AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    # Use a CharField or URLField to store image paths or URLs
    image = models.ImageField(upload_to='products/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

