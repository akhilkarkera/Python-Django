from django.urls import path, include
from myapp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register ("", UrlViewSet) # register method uses prefix and viewset 

urlpatterns = [
    path('url/', include(router.urls)), # include urls of router.urls
]