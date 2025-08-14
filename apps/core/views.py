from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from rest_framework import viewsets
from .models import Client, Contact, Prospection, Projet, Tache, ChiffreAffaire
from .serializers import (
    ClientSerializer, ContactSerializer, ProspectionSerializer,
    ProjetSerializer, TacheSerializer, ChiffreAffaireSerializer
)

def home_view(request):
    return render(request, "index.html")

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ProspectionViewSet(viewsets.ModelViewSet):
    queryset = Prospection.objects.all()
    serializer_class = ProspectionSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class ChiffreAffaireViewSet(viewsets.ModelViewSet):
    queryset = ChiffreAffaire.objects.all()
    serializer_class = ChiffreAffaireSerializer