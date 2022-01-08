# Generated by Django 3.2 on 2022-01-07 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerse', '0002_auto_20220107_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
        migrations.RemoveField(
            model_name='image',
            name='default',
        ),
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_pics',
        ),
        migrations.AddField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='multi_images',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='product_pics', to='ecommerse.product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ImageAlbum',
        ),
    ]