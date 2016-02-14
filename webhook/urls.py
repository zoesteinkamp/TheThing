from django.conf.urls import patterns, url
from webhook.views import *

urlpatterns = patterns('',
    url(r'^btc', btc, name='btc'),
    url(r'^travel', travel, name='travel'),
    url(r'^watson', watson, name='watson'),
    url(r'^intuit', intuit, name='intuit')
)

