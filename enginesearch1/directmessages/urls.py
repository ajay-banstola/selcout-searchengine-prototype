from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'directmessages'

urlpatterns = [
    #url(r'^inbox$', views.inbox, name='inbox'),
    url(r'^message$', views.Send_message, name='sent'),
    #url(r'^(', views.product_detail, name='product_detail'),
    #path('/account/', include('account.urls')),
]
