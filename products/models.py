from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.DecimalField(max_digits=4,decimal_places=0)
    product_name=models.CharField(max_length=50)
    product_price=models.DecimalField(max_digits=5,decimal_places=0)

    def __str__(self):
        return self.product_name