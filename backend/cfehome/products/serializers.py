from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from products.validators import validate_title, validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    # email = serializers.EmailField(write_only=True)
    # email = serializers.EmailField(source='user.email', read_only=True)
    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    name = serializers.CharField(source='title', read_only=True)
    body = serializers.CharField(source='content')
    
    class Meta:
        model = Product
        fields = [
            'pk',
            'owner',
            # 'user',
            'edit_url',
            'url',
            # 'email',
            'title',
            'name',
            # 'content',
            'body',
            'price',
            'sale_price',
            # 'my_discount',
            # 'my_user_data',
            # 'related_products',
            'public',
            'path',
            'endpoint',
        ]
    
    def get_my_user_data(self, obj):
        return {'username': obj.user.username}
    
    # field validation
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("{} is already a product name".format(value))
    #     return value
    
    # # create
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj
        
    # # update
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance
    
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
