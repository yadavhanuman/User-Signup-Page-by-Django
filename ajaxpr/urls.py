
from django.contrib import admin
from django.urls import path
from ajaxf.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('ajax_p/', ajax_p, name='ajax_p')
]
