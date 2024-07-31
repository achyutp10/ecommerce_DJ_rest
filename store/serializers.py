from rest_framework import serializers
from store.models import (
    Category, Product, ProductFaq, Gallery, Specification, Size, 
    Color, Cart, CartOrder, CartOrderItem, Review, Wishlist, Notification, Coupon
)
from userauths.serializers import ProfileSerializer
from vendor.models import Vendor

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"

# class ProductSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Product
#     fields = "__all__"
  

class GallerySerializer(serializers.ModelSerializer):
  class Meta:
    model = Gallery
    fields = "__all__"

class SpecificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Specification
    fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Size
    fields = "__all__"

class ColorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Color
    fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
  gallery = GallerySerializer(many=True, read_only=True)
  color = ColorSerializer(many=True, read_only=True) 
  specification = SpecificationSerializer(many=True, read_only=True)
  size = SizeSerializer(many=True, read_only=True)

  class Meta:
    model = Product
    fields = [
      'id', 'title', 'image', 'description', 'category', 'price', 'old_price', 'shipping_amount', 'stock_qty', 'in_stock', 'status', 'featured', 'views', 'rating', 'vendor', 'gallery', 'color', 'specification', 'size', 'pid', 'slug', 'date', 'product_rating','orders', 'rating_count',
    ]
  
  def __init__(self, *args, **kwargs):
    super(ProductSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cart
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(CartSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3



class CartOrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartOrderItem
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(CartOrderItemSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class CartOrderSerializer(serializers.ModelSerializer):
  orderitem = CartOrderItemSerializer(many=True, read_only=True)
  class Meta:
    model = CartOrder
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(CartOrderSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class ProductFaqSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductFaq
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(ProductFaqSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(VendorSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class ReviewSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer()
  class Meta:
    model = Review
    fields = ["id", "review", "rating", "reply", "user", "product", "profile", "date"]
  
  def __init__(self, *args, **kwargs):
    super(ReviewSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class WishlistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Wishlist
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(WishlistSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class CouponSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coupon
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(CouponSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = "__all__"
  
  def __init__(self, *args, **kwargs):
    super(NotificationSerializer, self).__init__(*args, **kwargs)

    request = self.context.get("request")
    if request and request.method == "POST":
      self.Meta.depth=0
    else:
      self.Meta.depth=3
  
class SummarySerializer(serializers.Serializer):
  product = serializers.IntegerField()
  order = serializers.IntegerField()
  revenue = serializers.DecimalField(max_digits=12, decimal_places=2)
  
class EarningSerializer(serializers.Serializer):
  monthly_revenue = serializers.DecimalField(max_digits=12, decimal_places=2)
  total_revenue = serializers.DecimalField(max_digits=12, decimal_places=2)
  
  
class CouponSummarySerializer(serializers.Serializer):
  total_coupons = serializers.IntegerField()
  active_coupons = serializers.IntegerField()

class NotificationSummarySerializer(serializers.Serializer):
  unread_noti = serializers.IntegerField()
  read_noti = serializers.IntegerField()
  all_noti = serializers.IntegerField()
  