from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    
    # for get url
    def get_url(self, obj):
        
        # static
        # return f"/api/products/{obj.pk}/"
        
        # dynamic
        request = self.context.get('request')
        print(request, 'test check')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)
    
    # for get edit url
    def get_edit_url(self, obj):
        request = self.context.get('request')
        print(request, 'test check')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

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
