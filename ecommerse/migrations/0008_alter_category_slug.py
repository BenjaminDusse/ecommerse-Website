# Generated by Django 3.2 on 2022-01-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerse', '0007_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
