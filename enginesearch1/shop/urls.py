from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import product_detail, product_list

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('/account/', include('account.urls')),
]
