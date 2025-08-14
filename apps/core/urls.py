from django.contrib import admin
from django.urls import path
from django.shortcuts import render
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

def home_view(request):
    return render(request, "index.html")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]