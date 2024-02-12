from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_category_for_product(category_pk):
    # кеширование
    if settings.CACHE_ENABLE:
        key = f'subject_list_{category_pk}'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.filter(product__category_id=category_pk)
            cache.set(key, category_list)
    else:
        category_list = Category.objects.filter(product__category_id=category_pk)
    return category_list
