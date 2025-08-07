# 🎯 Dashboard d'Agence Web - Crea2Code
🧑‍💻 Auteur
Crea2Code – Agence Web & Développement Python / Django

Ce projet est une application Django avec Django REST Framework (DRF) permettant de :
- Gérer les clients, contacts, prospections, projets, tâches et chiffre d'affaires.
- Utiliser une interface API (DRF) + une interface admin personnalisée.
- Centraliser la gestion de l'activité d'une agence freelance ou micro-entreprise.

## 🚀 Technologies utilisées

- Python 3
- Django 5.x
- Django REST Framework
- SQLite (dev) ou PostgreSQL (prod)
- HTML / Templates Django

---

## ✅ Fonctionnalités déjà en place

- [x] Modèles : `Client`, `Contact`, `Prospection`, `Projet`, `Tâche`, `ChiffreAffaire`
- [x] Interface admin personnalisée
- [x] API DRF avec `ViewSet` et `Router`
- [x] Page d’accueil (`home.html`)
- [x] Lien depuis admin vers page d’accueil

---

## 🧩 À faire / Bugs connus

- [ ] Ajouter un lien de retour vers la page d’accueil dans l’interface **DRF** (browsable API)
- [ ] Personnaliser l’interface API avec un menu
- [ ] Ajouter une page de login plus élégante (optionnel)
- [ ] Gérer les permissions dans l’API (lecture seule ou accès limité selon le rôle)
- [ ] Ajouter des filtres et recherches dans l’admin et l’API
- [ ] Ajouter des statistiques sur le dashboard (chiffre d'affaires mensuel, projets en cours...)

---

## ⚙️ Installation locale

```bash
git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd nom-du-repo
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sur Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
.
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       └── home.html
├── dashboard_agence/
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── README.md


