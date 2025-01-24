from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('', views.dashboard, name='dashboard'),  # Redirect root URL to the dashboard view
]