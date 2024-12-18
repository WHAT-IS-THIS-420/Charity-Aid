from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Custom registration view
    path('register/', views.register_view, name='register'),

    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Profile view
    path('profile/', views.profile_view, name='profile'),

    path('', views.profile_view, name='home'),


]
