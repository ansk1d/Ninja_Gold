from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('findgold', views.findgold),
    path('luckgold', views.luckgold)
]
