from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/', include('portfolio.urls')),

    url(r'', include('portfolio.urls', namespace='portfolio')),

    # Cart App URLs (MUST BE INCLUDED BEFORE SHOP APP URLS, SEE PAGE 227
    url(r'^cart/', include('cart.urls', namespace='cart')),

    # Orders App URLs, must be included before the shop URLS!
    url(r'^orders/', include('orders.urls', namespace='orders')),

    # Shop App URLs
    # Below is likely URL but will need to update
    url(r'^shop/', include('shop.urls', namespace='shop')),




    # GoodShepherd Code
    #   url(r'^accounts/login/$', views.login, name='login'),
    #   url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)