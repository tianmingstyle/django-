from django.conf.urls import url
from Api.views import *

urlpatterns=[
	url(r'savedata/',saveData),
	url(r'test/',test)
]