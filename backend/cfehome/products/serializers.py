from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # 'obj' is the instance of the 'product' model
    def get_my_discount(self, obj):
        try:
            if not hasattr(obj, 'id'):
                return None
            if not isinstance(obj, Product):
                return None
            return obj.get_discount()
        except:
            None
