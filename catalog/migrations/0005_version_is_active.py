# Generated by Django 5.0.1 on 2024-01-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активна'),
        ),
    ]
