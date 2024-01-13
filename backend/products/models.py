from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(null=True)
    
    @property
    def discount_price(self):
        return "%.2f" % (float(self.price) * 0.3)