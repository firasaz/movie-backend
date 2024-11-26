from django.urls import path
from .views import handshake

urlpatterns = [
    path('handshake/', handshake)
]