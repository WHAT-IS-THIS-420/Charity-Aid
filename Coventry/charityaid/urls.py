from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
]

