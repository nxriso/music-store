from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_brands, name='all_brands'),
    path('<str:brand_name>/', views.guitars, name='guitar_brands'),
    path(
        '<str:brand_name>/<str:guitar_model_name>/',
        views.show_details,
        name='show_details',
    ),
]
