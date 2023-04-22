"""michaelsmicros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import *
from cart.views import * #add_to_cart, cart, update_cart, remove_cart_item
from contact.views import contact


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('shop/', shop, name='shop'),
    path('remove_cart_item/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
    path('update_cart/', update_cart, name='update_cart'),
    path('submit_order/', submit_order, name='submit_order'),
    path('cart/', cart, name='cart'),
    path('contact/', contact, name='contact'),
    path('', include('cart.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
