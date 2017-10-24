from django.conf.urls import url
from . import views



from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^client/$', views.client_list, name='client_list'),

    url(r'^client/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),
    url(r'^client/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client/create/$', views.client_new, name='client_new'),
    url(r'^item/$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>\d+)/delete/$', views.item_delete, name='item_delete'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/create/$', views.item_new, name='item_new'),
    url(r'^employee/$', views.employee_list, name='employee_list'),
    url(r'^employee/(?P<pk>\d+)/delete/$', views.employee_delete, name='employee_delete'),
    url(r'^employee/(?P<pk>\d+)/edit/$', views.employee_edit, name='employee_edit'),
    url(r'^employee/create/$', views.employee_new, name='employee_new'),
    url(r'^donor/$', views.donor_list, name='donor_list'),
    url(r'^donor/(?P<pk>\d+)/delete/$', views.donor_delete, name='donor_delete'),
    url(r'^donor/(?P<pk>\d+)/edit/$', views.donor_edit, name='donor_edit'),
    url(r'^donor/create/$', views.donor_new, name='donor_new'),


    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$',
        login,
        name='login'),
    url(r'^logout/$',
        logout,
        name='logout'),
    url(r'^logout-then-login/$',
        logout_then_login,
        name='logout_then_login'),


    # change password urls
    url(r'^password-change/$',
        password_change,
        name='password_change'),
    url(r'^password-change/done/$',
        password_change_done,
        name='password_change_done'),

# restore password urls
    url(r'^password-reset/$',
        password_reset,
        name='password_reset'),
    url(r'^password-reset/done/$',
        password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'),
]