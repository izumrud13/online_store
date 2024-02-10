from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_category_for_product(product_pk):
    if settings.CACHE_ENABLE:
        key = f'subject_list_{product_pk}'
        category_list = cache.get(key)
        if category_list is None:
            subject_list = Category.object.filter(product_pk=product_pk)
            cache.set(key, category_list)
    else:
        category_list = Category.object.filter(product_pk=product_pk)

    return category_list
