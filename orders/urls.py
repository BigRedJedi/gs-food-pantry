from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$',
        views.order_create,
        name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/$',
        views.admin_order_detail,
        name='admin_order_detail'),
    ]

# Add more code from where stopped on page 239
# May need to work with templates and CSS files on page 270
