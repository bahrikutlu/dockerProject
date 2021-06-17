from django.contrib import admin
from django.urls import path
from . import views_core

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', views_core.home)
]