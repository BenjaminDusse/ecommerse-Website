# Generated by Django 3.2 on 2022-01-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='shipping_region',
            name='shipping_id',
        ),
        migrations.RemoveField(
            model_name='shipping_type',
            name='shipping_type_id',
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='corp_id',
            field=models.PositiveBigIntegerField(),
        ),
    ]
