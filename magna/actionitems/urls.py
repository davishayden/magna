
from django.conf.urls import url

from . import views
app_name = 'actionitem'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^(?P<line_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<line_id>[0-9]+)/new/$', views.new, name='new'),
]