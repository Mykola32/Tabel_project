from django.urls import path, include

from app1.views import *

urlpatterns = [
    path('', index, name='index'),
    path('logforma/', logforma, name='logforma'),
]