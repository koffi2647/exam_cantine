from django.urls import path
from .urls import views

app_name = 'plat'
urlpatterns = [
    path('', views.plat_list, name='plat_list'),
    path('create/', views.plat_create, name='plat_create'),
    path('<str:pk>/update/', views.plat_update, name='plat_update'),
    path('<str:pk>/delete/', views.plat_delete, name='plat_delete'),
]
