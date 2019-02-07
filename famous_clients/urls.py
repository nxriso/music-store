from django.urls import path
from . import views

urlpatterns = [
    path('', views.famous_customers, name='famous_customers')
]
