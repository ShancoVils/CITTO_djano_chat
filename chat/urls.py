from django.urls import path

from . import views

urlpatterns = [
    path('', views.hub, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('chat-list/', views.list, name='list'),
]