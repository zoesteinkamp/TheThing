from django.conf.urls import patterns, url, include
from webhook import views

urlpatterns = patterns('',

    url(r'^webhook', webhook.as_view()),

)

