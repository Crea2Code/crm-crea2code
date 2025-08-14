FROM ubuntu:latest
LABEL authors="chala"

ENTRYPOINT ["top", "-b"]
# Utiliser une image officielle Python comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier le fichier requirements.txt dans le container
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le container
COPY . .

# Exposer le port 8000
EXPOSE 8000

# Commande pour lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
