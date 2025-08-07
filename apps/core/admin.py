from django.contrib import admin
from .models import Client, Contact, Prospection, Projet, Tache, ChiffreAffaire

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'company', 'created_at')
    search_fields = ('nom', 'email', 'company')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'fonction', 'client')
    search_fields = ('nom', 'email', 'client__nom')


@admin.register(Prospection)
class ProspectionAdmin(admin.ModelAdmin):
    list_display = ('client', 'statut', 'date_contact')
    list_filter = ('statut',)
    search_fields = ('client__nom',)


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'client', 'statut', 'date_debut', 'date_fin')
    list_filter = ('statut',)
    search_fields = ('nom', 'client__nom')


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('titre', 'projet', 'terminee', 'echeance')
    list_filter = ('terminee',)
    search_fields = ('titre', 'projet__nom')


@admin.register(ChiffreAffaire)
class ChiffreAffaireAdmin(admin.ModelAdmin):
    list_display = ('client', 'montant', 'date')
    search_fields = ('client__nom',)
    date_hierarchy = 'date'