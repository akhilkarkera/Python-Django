
from django.urls import path, include
from myapp import views


urlpatterns = [
    path('', views.Make, name = "Make"),
    path('<str:token>', views.Home, name="Home"),
]
