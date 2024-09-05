from django.urls import path
from .urls import views

app_name = 'menu'
urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('create/', views.menu_create, name='menu_create'),
    path('<str:pk>/update/', views.menu_update, name='menu_update'),
    path('<str:pk>/delete/', views.menu_delete, name='menu_delete'),
]
