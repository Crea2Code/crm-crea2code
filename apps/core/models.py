from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contacts')
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    fonction = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.client})"


class Prospection(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    statut = models.CharField(max_length=50, choices=[
        ('en_cours', 'En cours'),
        ('converti', 'Converti'),
        ('abandonne', 'Abandonné')
    ])
    date_contact = models.DateField()
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} - {self.statut}"


class Projet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé')
    ])

    def __str__(self):
        return self.nom


class Tache(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    terminee = models.BooleanField(default=False)
    echeance = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.titre} ({'✓' if self.terminee else '✗'})"


class ChiffreAffaire(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} - {self.montant} €"