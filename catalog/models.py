from django.db import models

# Create your models here.
NULLABLE = {
    'blank': True,
    'null': True,
}



class Category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='product/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    cost = models.IntegerField(verbose_name='Цена')
    first_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return f'{self.name} | {self.category} | {self.cost} руб.'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('category',)
