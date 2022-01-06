import datetime
    
from django.db import models
from django.core.validators import FileExtensionValidator
from django_resized import ResizedImageField
from django.utils import timezone
from django.contrib.auth.models import User


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    url = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Manufacturer(models.Model):
    corp_id = models.PositiveIntegerField()
    shop_id = models.PositiveBigIntegerField()
    business_license_register_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product/product_pics/")
    default = models.BooleanField(default=False)
    width = models.FloatField(
        default=450, help_text="If for list: 220x220 or for detail 450x450")
    height = models.FloatField(
        default=450, help_text="If for list: 220x220 or for detail 450x450")
    album = models.ForeignKey(
        ImageAlbum, related_name='images', on_delete=models.CASCADE
    )


class Measurements(models.Model):
    name = models.CharField(max_length=200)
    size_in_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='product/videos/', null=True, blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image = ResizedImageField(size=[220, 220], upload_to='product/image/')
    product_pics = models.ImageField(upload_to="product/product_pics/", )
    models.OneToOneField(ImageAlbum, related_name='model',
                         on_delete=models.CASCADE)
    manufacturer = models.OneToOneField(
        Manufacturer,
        on_delete=models.CASCADE,
        null=True
    )
    album = models.OneToOneField(
        ImageAlbum, related_name='model', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='product_tags')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='product_category')
    # product_colors = models.ManyToManyField(
    #     Product_color, related_name='product_color')
    # edit both after create and add fields into User model
    likes = models.ManyToManyField(User, related_name='product_likes')
    dislikes = models.ManyToManyField(User, related_name='product_dislikes')
    url = models.SlugField(max_length=300, unique=True)
    # views # add views correctly
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ManyToManyField(Measurements, related_name='product_sizes')
    is_available = models.BooleanField(default=False)
    

class Product_color(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_color')

    def __str__(self):
        return self.name


class Specifications(models.Model):
    brand_name = models.CharField(max_length=300)
    applicable_season = models.CharField(max_length=200)
    wool = models.CharField(max_length=200)
    pattern_type = models.CharField(max_length=300)
    collar = models.CharField(max_length=300)
    technics = models.CharField(max_length=300)
    sleeve_style = models.CharField(max_length=300)
    is_hooded = models.BooleanField(default=False)
    color = models.CharField(max_length=300)
    material_type = models.CharField(max_length=300)
    type_more = models.CharField(max_length=500)
    measurement_unit = models.CharField(max_length=500)
    each_pack = models.PositiveIntegerField()
    package_size_length = models.PositiveIntegerField(default=1)
    package_size_width = models.PositiveIntegerField(default=1)
    origin = models.CharField(max_length=200)
    material = models.CharField(max_length=300)
    style = models.CharField(max_length=300)
    closure_type = models.CharField(max_length=300)  # add other fields

    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.brand_name


class Discount(models.Model):
    date_created = models.DateTimeField(default=timezone.now())
    is_sale = models.BooleanField(default=False)
    discount_percent = models.FloatField(default=0.5)
    is_new = models.BooleanField(default=True)
    discount = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def was_published_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=30)


class Shipping_Region(models.Model):
    shipping_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # from product using google maps
    shipping_price = models.CharField(max_length=200)
    product_regions = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='product_shipping_type')

    def __str__(self):
        return self.name


class Shipping_type(models.Model):
    shipping_type_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    shopping_days_count = models.DateTimeField(default=3)
    shipping_regions = models.ManyToManyField(
        Shipping_Region,  related_name='region_shipping_type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shipping_type'
        verbose_name_plural = 'Shipping_types'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(
        Product, verbose_name="product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Shared_links(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='product_links')
    facebook = models.CharField(max_length=300)
    pinterest = models.CharField(max_length=300)
    vk = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    slug = models.SlugField(max_length=500)

    def __str__(self):
        return self.slug

    # need set slugify


class Service(models.Model):
    service_id = models.PositiveIntegerField()
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    icon = models.ImageField(upload_to='product/service/')
    banner = models.ImageField(upload_to='product/service/')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='additional_product_service')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'


class Order(models.Model):
    STATUS_DELIVERY_CHOICES = (
        ('in order', 'in order'),
        ('Confirmed', 'Confirmed'),
        ('pending', 'pending'),
        ('On the way', 'On the way'),
        ('Completed', 'Completed'),
        ('Unshipped', 'Unshipped'),
        ('Canceled', 'Canceled'),
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_order')
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_customer')
    status = models.CharField(max_length=300, choices=STATUS_DELIVERY_CHOICES)

    def __str__(self):
        return f"{self.customer.name} ordered {self.product.title}"

# add Basemodel into models
# add_rating and rating_stars
