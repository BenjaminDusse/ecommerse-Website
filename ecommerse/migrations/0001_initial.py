# Generated by Django 3.2 on 2022-01-07 14:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('url', models.SlugField(blank=True, max_length=200, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerse.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('corp_id', models.PositiveIntegerField()),
                ('shop_id', models.PositiveBigIntegerField()),
                ('business_license_register_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('size_in_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('product_id', models.PositiveBigIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(blank=True, null=True, upload_to='product/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('image', models.ImageField(upload_to='product/image/')),
                ('url', models.SlugField(max_length=300, unique=True)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_available', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='ecommerse.category')),
                ('dislikes', models.ManyToManyField(related_name='product_dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='product_likes', to=settings.AUTH_USER_MODEL)),
                ('manufacturer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerse.manufacturer')),
                ('product_pics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='ecommerse.imagealbum')),
                ('size', models.ManyToManyField(related_name='product_sizes', to='ecommerse.Measurements')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('value', models.SmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Rating Star',
                'verbose_name_plural': 'Rating Stars',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Shipping_Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('shipping_price', models.CharField(max_length=200)),
                ('product_regions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_shipping_type', to='ecommerse.product')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=300)),
                ('applicable_season', models.CharField(max_length=200)),
                ('wool', models.CharField(max_length=200)),
                ('pattern_type', models.CharField(max_length=300)),
                ('collar', models.CharField(max_length=300)),
                ('technics', models.CharField(max_length=300)),
                ('sleeve_style', models.CharField(max_length=300)),
                ('is_hooded', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=300)),
                ('material_type', models.CharField(max_length=300)),
                ('type_more', models.CharField(max_length=500)),
                ('measurement_unit', models.CharField(max_length=500)),
                ('each_pack', models.PositiveIntegerField()),
                ('package_size_length', models.PositiveIntegerField(default=1)),
                ('package_size_width', models.PositiveIntegerField(default=1)),
                ('origin', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=300)),
                ('style', models.CharField(max_length=300)),
                ('closure_type', models.CharField(max_length=300)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerse.product')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_type_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('shopping_days_count', models.DateTimeField(default=3)),
                ('shipping_regions', models.ManyToManyField(related_name='region_shipping_type', to='ecommerse.Shipping_Region')),
            ],
            options={
                'verbose_name': 'Shipping_type',
                'verbose_name_plural': 'Shipping_types',
            },
        ),
        migrations.CreateModel(
            name='Shared_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=300)),
                ('pinterest', models.CharField(max_length=300)),
                ('vk', models.CharField(max_length=300)),
                ('twitter', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=500)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_links', to='ecommerse.product')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('service_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=5000)),
                ('icon', models.ImageField(upload_to='product/service/')),
                ('banner', models.ImageField(upload_to='product/service/')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='additional_product_service', to='ecommerse.product')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=5000)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='ecommerse.reviews', verbose_name='parent')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerse.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=15)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='ecommerse.product')),
                ('review', models.ManyToManyField(blank=True, related_name='reviews', to='ecommerse.Reviews')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerse.ratingstar')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Product_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_color', to='ecommerse.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='product_tags', to='ecommerse.Tags'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('in order', 'in order'), ('Confirmed', 'Confirmed'), ('pending', 'pending'), ('On the way', 'On the way'), ('Completed', 'Completed'), ('Unshipped', 'Unshipped'), ('Canceled', 'Canceled')], max_length=300)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_customer', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='ecommerse.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='product/product_pics/')),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=450, help_text='If for list: 220x220 or for detail 450x450')),
                ('height', models.FloatField(default=450, help_text='If for list: 220x220 or for detail 450x450')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ecommerse.imagealbum')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_sale', models.BooleanField(default=False)),
                ('discount_percent', models.FloatField(default=0.5)),
                ('is_new', models.BooleanField(default=True)),
                ('discount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerse.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]