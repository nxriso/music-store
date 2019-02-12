from django.contrib import admin
from django.urls import include, path

from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', include('contact.urls')),
    path('all-branch/', include('instruments.urls')),
    path('famous-customers', include('famous_clients.urls')),
    path('payment-methods/', views.payment_methods, name='payment-methods'),
    path('admin/', admin.site.urls),
]
