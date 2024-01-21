from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=150, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    first_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    sign_publications = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} | {self.view_count}'

    class Meta:
        verbose_name = 'блог'
