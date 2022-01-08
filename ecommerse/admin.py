from django.contrib import admin
from ecommerse.models import (
    Tags,
    Category,
    Manufacturer,
    Measurements,
    Product,
    Product_color,
    Specifications,
    Discount,
    Shipping_Region,
    Shipping_type,
    Reviews,
    Shared_links,
    Service,
    Order,
    RatingStar,
    Rating,
    Image
)

admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Measurements)
admin.site.register(Product_color)
admin.site.register(Specifications)
admin.site.register(Discount)
admin.site.register(Shipping_Region)
admin.site.register(Shipping_type)
admin.site.register(Reviews)
admin.site.register(Shared_links)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(RatingStar)
admin.site.register(Rating)


class ProductImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    
    
    class Meta:
        model = Product
# Images for product tagline images
# admin.site.register(Image)