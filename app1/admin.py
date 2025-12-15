from django.contrib import admin
from .models import Contact, Product, ProductImage, ProductVariant, Review, Wishlist, Blog,Order,OrderItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('user_name','rating','body','created_at')
    can_delete = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale', 'stock', 'created_at', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductImageInline, ProductVariantInline, ReviewInline]
    search_fields = ('title',)

admin.site.register(Contact)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(Review)
admin.site.register(Wishlist)

admin.site.register(Blog)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_amount", "payment_method", "payment_status", "created_at")
    inlines = [OrderItemInline]