# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('polls/', include('polls.urls')),
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('signup/', views.register),
    path('base/', views.base),
    path('send/', views.sendSimpleEmail),
]
