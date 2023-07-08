from django.urls import path
from .views import index, page1

urlpatterns = [
    path('', index),
    path('page1/', page1)
]