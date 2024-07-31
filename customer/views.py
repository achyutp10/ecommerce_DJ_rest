from django.shortcuts import render, redirect
import requests
from store.models import Category, Product, ProductFaq, Gallery, Specification, Size, Color, Cart, CartOrder, CartOrderItem, Review, Wishlist, Notification, Coupon, Tax
from store.serializers import ProductSerializer, CategorySerializer, CartSerializer, CartOrderSerializer,CartOrderItemSerializer, CouponSerializer, ReviewSerializer, NotificationSerializer, WishlistSerializer

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from userauths.models import User
from decimal import Decimal
from rest_framework.response import Response
import stripe
from django.conf import settings

class OrdersAPIView(generics.ListAPIView):
  serializer_class = CartOrderSerializer
  permission_classes = [AllowAny]
  
  def get_queryset(self):
    user_id = self.kwargs['user_id']
    user = User.objects.get(user=user_id)

    orders = CartOrder.objects.filter(buyer=user, payment_status="paid")
    return orders

class OrderDetailAPIView(generics.RetrieveAPIView):
  serializer_class = CartOrderSerializer
  permission_classes = [AllowAny]

  
  def get_queryset(self):
    user_id = self.kwargs['user_id']
    order_oid = self.kwargs["order_oid"]
    user = User.objects.get(user=user_id)

    order = CartOrder.objects.get(buyer=user, oid=order_oid, payment_status="paid")
    return order


class WishlistAPIView(generics.ListCreateAPIView):
  serializer_class = WishlistSerializer
  permission_classes = [AllowAny]
  
  def get_queryset(self):
    user_id = self.kwargs['user_id']
    user = User.objects.get(id=user_id)
    wishlist = Wishlist.objects.filter(user=user)
    return wishlist
  
  def create(self, request, *args, **kwargs):
    payload = request.data

    product_id = payload['product_id']
    user_id = payload['user_id']

    product = Product.objects.get(id=product_id)
    user = User.objects.get(id=user_id)

    wishlist = Wishlist.objects.filter(user=user, product=product)
    if wishlist:
      wishlist.delete()
      return Response({"error": "Wishlist Deleted Successfully"}, status=status.HTTP_200_OK)
    else:
      Wishlist.objects.create(product=product, user=user)
      return Response({"message": "Product added to wishlist"}, status=status.HTTP_201_CREATED)

class CustomerNotification(generics.ListAPIView):
  serializer_class = NotificationSerializer
  permission_classes = [AllowAny]
  
  def get_queryset(self):
    user_id = self.kwargs['user_id']
    user = User.objects.get(id=user_id)
    return Notification.objects.filter(user=user, seen=False)

class MarkCustomerNotificationAsSeen(generics.RetrieveAPIView):
  serializer_class = NotificationSerializer
  permission_classes = [AllowAny]

  def get_object(self):
    user_id = self.kwargs['user_id']
    notifi_id = self.kwargs['notifi_id']
    user = User.objects.get(id=user_id)
    noti = Notification.objects.get(id=notifi_id, user=user)
    if noti.seen != True:
      noti.seen = True
      noti.save()
    
    return noti


    
  