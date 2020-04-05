from django.db import models

# Create your models here.
class Buy(models.Model):
    cust_name=models.CharField(max_length=70)
    product_id=models.DecimalField(max_digits=4,decimal_places=0)

    def __str__(self):
        return self.cust_name
    
