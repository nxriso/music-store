from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-brands/', include('instruments.urls')),
    path('payment-methods/', views.payment_methods, name='payment-methods'),
    path('admin/', admin.site.urls),
]
