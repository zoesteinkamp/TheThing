from django.conf.urls import patterns, url
from webhook.views import webhook

urlpatterns = patterns('',
                       url(r'^webhook', webhook),
)

