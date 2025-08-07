from rest_framework import serializers
from .models import Client, Contact, Prospection, Projet, Tache, ChiffreAffaire

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ProspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospection
        fields = '__all__'

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = '__all__'

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'

class ChiffreAffaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiffreAffaire
        fields = '__all__'