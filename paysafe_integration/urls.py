from django.contrib import admin
from django.urls import path,include
from .settings import ADMIN_ENABLED


urlpatterns = [
    path('',include('paysafe.urls'))

]

if ADMIN_ENABLED:
    urlpatterns.append(path('admin/', admin.site.urls))
