from django.conf.urls import patterns, url, include
from webhook.views import webhook

urlpatterns = patterns('',

    url(r'^webhook', webhook),

)

