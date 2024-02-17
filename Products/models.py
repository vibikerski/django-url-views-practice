from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    
    def __str__(self):
        return self.name

def validate_rating(value):
    if value < 0 or value > 5:
        raise ValidationError("Rating must be between 0 and 5.")

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(validators=[validate_rating])
    
    def __str__(self):
        return f"{self.product.name} review by {self.author}"