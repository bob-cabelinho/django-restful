from rest_framework import serializers

from .models import Product

def validate_title(value):
    queryset = Product.objects.filter(title__iexact=value)
    if queryset.exists():
        raise serializers.ValidationError(f"This {value} already exists on Data Base!")
    return value