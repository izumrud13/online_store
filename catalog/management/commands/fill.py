from django.core.management import BaseCommand
from catalog.models import Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        catalog_list =[
            {"category_name": "Телефоны", "description": "Наличие уточнять у менеджера"},
            {"category_name": "Планшеты", "description": "Наличие уточнять у менеджера"},
            {"category_name": "Смарт часы", "description": "Наличие уточнять у менеджера"},
            {"category_name": "Наушники", "description": "Наличие уточнять у менеджера"},
            {"category_name": "Ноутбуки", "description": "Наличие уточнять у менеджера"},
            {"category_name": "Аксессуары", "description": "Наличие уточнять у менеджера"},
        ]

        catalog_for_create =[]
        for item in catalog_list:
            catalog_for_create.append(
                Category(**item)
            )

        print(catalog_for_create)

        Category.objects.bulk_create(catalog_for_create)
