import datetime
import random
import string


from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from shared.django.model import BaseModel, DeleteModel


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Tags, self).save(*args, **kwargs)

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
    description = models.TextField(max_length=5000, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Manufacturer(BaseModel):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=155)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class Measurements(models.Model):
    name = models.CharField(max_length=200)
    size_in_number = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='product/videos/', null=True, blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image = models.ImageField(upload_to='product/image/')
    manufacturer = models.OneToOneField(
        Manufacturer,
        on_delete=models.CASCADE,
        null=True
    )
    tags = models.ManyToManyField(Tags, related_name='product_tags')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name='product_category')
    likes = models.ManyToManyField(User, related_name='product_likes')
    dislikes = models.ManyToManyField(User, related_name='product_dislikes')
    url = models.SlugField(max_length=300, unique=True)
    # views # add views correctly
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ManyToManyField(Measurements, related_name='product_sizes')
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Image(BaseModel):
    image = models.ImageField(upload_to="product/product_pics/")
    multi_images = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_pics')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


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


class Discount(BaseModel):
    is_sale = models.BooleanField(default=False)
    discount_percent = models.FloatField(default=0.5)
    is_new = models.BooleanField(default=True)
    discount = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def was_published_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=30)


class Shipping_Region(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # from product using google maps
    shipping_price = models.CharField(max_length=200)
    product_regions = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='product_shipping_type')

    def __str__(self):
        return self.name


class Shipping_type(models.Model):
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


class Reviews(BaseModel):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="parent", on_delete=models.SET_NULL, null=True, blank=True, related_name='children'
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


class Service(BaseModel):
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


class Order(BaseModel):
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


class RatingStar(BaseModel):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Rating Star"
        verbose_name_plural = "Rating Stars"
        ordering = ["-value"]


class Rating(BaseModel):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="ratings", null=True, blank=True)
    review = models.ManyToManyField(
        Reviews, related_name='reviews', blank=True)

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


# product pics da Frontend chi manga multiple rasm qo'sha oladigan qilib berishi kerak shunda API ishlaydi to'g'ri
