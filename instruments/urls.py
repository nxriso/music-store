from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guitars, name='all_guitars'),
    path('<int:guitar_id>/', views.show_details, name='show_details')

]
