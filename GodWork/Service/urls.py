from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'content/(?P<ids>\d+)',content),
    url(r'list/',list) 
]
