

# # # https://gemini.google.com/app/6db35aae43a64f70
# # # https://gemini.google.com/app/6db35aae43a64f70

# # https://gemini.google.com/app/6db35aae43a64f70
# # https://gemini.google.com/app/6db35aae43a64f70
# # https://gemini.google.com/app/6db35aae43a64f70
# # https://gemini.google.com/app/6db35aae43a64f70
# # https://gemini.google.com/app/6db35aae43a64f70

# # https://gemini.google.com/app/6db35aae43a64f70
# # https://gemini.google.com/app/6db35aae43a64f70
# # https://gemini.google.com/app/6db35aae43a64f70

# # https://gemini.google.com/app/6db35aae43a64f70


# # https://gemini.google.com/app/8db05da3c2cf0a52
# # https://gemini.google.com/app/8db05da3c2cf0a52
# # https://gemini.google.com/app/8db05da3c2cf0a52
# # https://gemini.google.com/app/8db05da3c2cf0a52
# # https://gemini.google.com/app/8db05da3c2cf0a52

# # https://gemini.google.com/app/8db05da3c2cf0a52
# # https://gemini.google.com/app/8db05da3c2cf0a52



            
            
            
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# https://gemini.google.com/app/8db05da3c2cf0a52
# https://gemini.google.com/app/8db05da3c2cf0a52
# https://gemini.google.com/app/8db05da3c2cf0a52
# https://gemini.google.com/app/8db05da3c2cf0a52
# https://gemini.google.com/app/8db05da3c2cf0a52






# 2. Rappel de l'architecture globale

# Pour que tout fonctionne, votre projet doit respecter cette structure de fichiers :
# Fichier	Rôle
# models.py	Stocke les Utilisateurs, les Menus et la table de liaison MenuAcces.
# views.py	Calcule qui a droit à quoi et traite les formulaires (POST).
# urls.py	Dirige les clics sur les boutons vers les bonnes fonctions Python.
# page_utilisateur.html	Affiche la Navbar dynamique et la Matrice de cases à cocher.
# admin_extras.py	(Filtre) Permet au template de lire le dictionnaire des accès.

from app_contact.models import User




class Menu(models.Model):
    nom = models.CharField(max_length=100)
    code_menu = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class MenuAcces(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    est_visible = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'menu')

# Signal : Crée automatiquement les accès (masqués) pour chaque nouveau menu existant
@receiver(post_save, sender=User)
def create_menu_access_for_new_user(sender, instance, created, **kwargs):
    if created:
        menus = Menu.objects.all()
        for menu in menus:
            MenuAcces.objects.get_or_create(user=instance, menu=menu, defaults={'est_visible': False})
            
            
                    