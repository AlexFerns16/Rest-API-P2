from algoliasearch_django import AlgoliaIndex
from products.models import Product
from algoliasearch_django.decorators import register

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        # 'content',
        'body',
        'price',
        'user',
        'public',
        'path',
        'endpoint',
    ]

    settings = {
        # 'searchableAttributes': ['title', 'content'],
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public']
    }
    tags = 'get_tags_list'
