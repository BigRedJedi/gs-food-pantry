from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/', include('portfolio.urls')),

    url(r'', include('portfolio.urls', namespace='portfolio')),

    # GoodShepherd Code
    #   url(r'^accounts/login/$', views.login, name='login'),
    #   url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

]