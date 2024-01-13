from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    class Meta:
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
        return obj.price * 0.8