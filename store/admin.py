from django.contrib import admin

# Register your models here.
from store.models import Product, Category, Gallery, Specification, Size, Color, Cart, CartOrder, CartOrderItem, ProductFaq, Review, Wishlist, Notification,  Coupon, Tax

class GalleryInline(admin.TabularInline):
  model = Gallery
  extra = 0

class SpecificationInline(admin.TabularInline):
  model = Specification
  extra = 0

class SizeInline(admin.TabularInline):
  model = Size
  extra = 0

class ColorInline(admin.TabularInline):
  model = Color
  extra = 0

class CartOrderItemsInlineAdmin(admin.TabularInline):
    model = CartOrderItem

class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'price', 'category', 'shipping_amount', 'stock_qty', 'in_stock', 'vendor', 'featured']
  list_editable = ['featured']
  list_filter = ['date']
  search_fields = ['title']
  inlines = [GalleryInline, SpecificationInline, SizeInline, ColorInline]

class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart_id', 'qty', 'price', 'sub_total' , 'shipping_amount', 'service_fee', 'tax_fee', 'total', 'country', 'size', 'color', 'date']

class CartOrderAdmin(admin.ModelAdmin):
    inlines = [CartOrderItemsInlineAdmin]
    search_fields = ['oid', 'full_name', 'email', 'mobile']
    list_editable = ['order_status', 'payment_status']
    list_filter = ['payment_status', 'order_status']
    list_display = ['oid', 'payment_status', 'order_status', 'sub_total', 'shipping_amount', 'tax_fee', 'service_fee' ,'total', 'saved' ,'date']


class CartOrderItemsAdmin(admin.ModelAdmin):
    # list_filter = ['delivery_couriers', 'applied_coupon']
    # list_editable = ['date']
    list_display = ['order_id', 'vendor', 'product' ,'qty', 'price', 'sub_total', 'shipping_amount' , 'service_fee', 'tax_fee', 'total', 'date']

class ProductFaqAdmin(admin.ModelAdmin):
    list_editable = [ 'active', 'answer']
    list_display = ['user', 'question', 'answer' ,'active']

class ProductReviewAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_editable = ['active']
    list_display = ['user', 'product', 'review', 'reply' ,'rating', 'active']

class NotificationAdmin(admin.ModelAdmin):
    list_editable = ['seen']
    list_display = ['order', 'seen', 'user', 'vendor', 'date']

class NotificationAdmin(admin.ModelAdmin):
    list_editable = ['seen']
    list_display = ['order', 'seen', 'user', 'vendor', 'date']

# class CouponUsersInlineAdmin(admin.TabularInline):
#     model = Coupon

# class CouponAdmin(admin.ModelAdmin):
#     inlines = [CouponUsersInlineAdmin]
#     list_editable = ['code', 'active', ]
#     list_display = ['vendor' ,'code', 'discount', 'active', 'date']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemsAdmin)
admin.site.register(ProductFaq, ProductFaqAdmin)
admin.site.register(Review, ProductReviewAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Tax)
# admin.site.register(Coupon, CouponAdmin)

admin.site.register(Wishlist)