from rest_framework import routers
from django.urls import path, include
from .views import ClientViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet,  basename='client')

urlpatterns = [
    path('', include(router.urls)),
]
