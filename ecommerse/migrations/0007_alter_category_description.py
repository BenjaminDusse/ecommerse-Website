# Generated by Django 3.2 on 2022-01-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerse', '0006_auto_20220108_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]