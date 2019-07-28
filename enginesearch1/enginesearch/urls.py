"""enginesearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from account.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^index/$', home),
    #url(r'^$', lan),
    url(r'^prodform/$', products,name='productform'),
    url(r'^register/$', custreg, name='register'),
    url(r'^login/$', login, name='login'),
    path('cart/', include('cart.urls')),
    url(r'^logout/$', logout,name='logout'),
    path('index/', include('shop.urls', namespace = 'shop')),
    path('account/', include('account.urls', namespace = 'account')),
    path('directmessage/', include('directmessages.urls', namespace='message')),
    path('', include('landingpage.urls', namespace = 'landingpage')),
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

