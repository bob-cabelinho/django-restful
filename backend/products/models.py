from django.db import models

class ProductManager(models.Manager):

    def search(self, query):
        return Product.objects.filter(public=True, title_icontains=query)

class Product(models.Model):
    '''
    A model implements a PRODUCT.
    Table: Product
    Columns:
        + title
        + price
        + description
    '''
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(null=True)
    public = models.BooleanField(default=True)

    @property
    def discount_price(self):
        '''
        Function to get price after applying discount.
        '''
        return "%.2f" % (float(self.price) * 0.8)
