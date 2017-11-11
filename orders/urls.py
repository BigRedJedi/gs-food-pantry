from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$',
        views.order_create,
        name='order_create'),
    ]

# Add more code from where stopped on page 239
# May need to work with templates and CSS files on page 270
