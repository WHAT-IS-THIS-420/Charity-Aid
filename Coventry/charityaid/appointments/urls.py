from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.view_appointments, name='view_appointments'),
    path('schedule/', views.schedule_appointment, name='schedule_appointment'),
    path('edit/<int:pk>/', views.edit_appointment, name='edit_appointment'),
    path('', views.index, name='index'),
    path('recipiant', views.recipiants_list, name='recipiant_list'),
    path('recipiant/<int:id>/', views.recipiants_detail, name="recipiant_detail"),
    path('recipiant/<int:id>/edit', views.recipiants_edit, name="recipiant_edit"),
    path('recipiant/<int:id>/delete', views.recipiants_delete, name="recipiant_delete"),
]