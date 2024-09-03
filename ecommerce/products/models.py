from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOICES=(
    ('BC','buttercake'),
    ('BM','buttermilk'),
    ('CS','chesseslice'),
    ('CO','cococola'),
    ('CG','cowgheee'),
    ('CU','curd'),
    ('IC','icecreams'),
    ('KU','kulfi'),
    ('LA','lays'),
    ('MA','maggi'),
    ('MS','milkshake'),
    ('SB','sweetbox'),
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    ratings=models.FloatField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='items')
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity*self.product.price