from django.conf.urls import url

from search.views import *

app_name='search'

urlpatterns = [
	url(r'', search, name='search'),
	]