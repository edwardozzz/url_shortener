from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.link_list, name='link_list'),
    path('<str:short_url>/', views.redirect_to_original, name='redirect'),
]
