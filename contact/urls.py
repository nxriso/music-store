from django.urls import path

from contact import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks')
]
