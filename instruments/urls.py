from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_brands, name='all_brands'),
    path('<slug:brand_slug>/', views.guitars, name='guitar_brands'),
    path(
        '<slug:brand_slug>/<slug:guitar_slug>/',
        views.show_details,
        name='show_details',
    ),
]
