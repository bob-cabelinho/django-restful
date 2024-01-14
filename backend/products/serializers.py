from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title

class ProductSerializer(serializers.ModelSerializer):
    '''
    Serializer to Product model.
    '''
    title = serializers.CharField(validators=[validate_title])
    discount_price = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        '''
        Product 'Schema'
        '''
        model = Product
        fields = [
            "pk",
            "url",
            "title",
            "price",
            "description",
            "discount_price"
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_discount_price(self, obj):
        if not hasattr(obj, "id"):
            return None
