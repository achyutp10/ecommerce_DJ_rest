"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#DRF-YASG Documentation Code Snippet (In Project urls.py)
# drf-yasg imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Notes Backend APIs",
      default_version='v1',
      description="This is the API documentation for Achyut Notes Sharing Project APIs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="achyutp10@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    # path('userauths/', include('userauths.urls')),
    # path('store/', include('store.urls')),
    # path('vendor/', include('vendor.urls')),
    # path('cart/', include('cart.urls')),

    # Documentation
      path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
