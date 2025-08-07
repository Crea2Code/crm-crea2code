from rest_framework import routers
from django.urls import path, include
from .views import  (
    ClientViewSet, ContactViewSet, ProspectionViewSet,
    ProjetViewSet, TacheViewSet, ChiffreAffaireViewSet
)

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'prospections', ProspectionViewSet)
router.register(r'projets', ProjetViewSet)
router.register(r'taches', TacheViewSet)
router.register(r'chiffres-affaires', ChiffreAffaireViewSet)

urlpatterns = [
    path('', include(router.urls)),
]