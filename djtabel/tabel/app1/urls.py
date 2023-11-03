from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app1.views import *

urlpatterns = [
    path('', index, name='index'),
    path('logforma/', logforma, name='logforma'),
    path('logforma/menu_after_form/', create_check, name='create_check'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)