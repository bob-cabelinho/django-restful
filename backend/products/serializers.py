from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    '''
    Serializer to Product model.
    '''
    discount_price = serializers.SerializerMethodField()
    class Meta:
        '''
        Product 'Schema'
        '''
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "description",
            "discount_price"
        ]

    def discount_price(self, obj):

        if not isinstance(obj, Product):
            return None
        return obj.discount_price(obj.price)
