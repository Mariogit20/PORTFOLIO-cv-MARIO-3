from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User, Menu, MenuAcces
from app_contact.models import Contact
from PackageUser.modul_new_user import GestionnaireUtilisateur
import re

# --- UTILITAIRES ---

# --- VUE PRINCIPALE (GESTION GLOBALE) ---

# N'oubliez pas d'importer le modèle Role en haut du fichier


from app_contact.models import Role 



def gestion_globale(request):
    """
    Affiche la page d'administration avec les utilisateurs, 
    les menus et les messages de contact.
    """
    users = User.objects.all()
    menus = Menu.objects.all()
    contacts = Contact.objects.all().order_by('-date_envoi')
    
    # --- AJOUT CRUCIAL ICI ---
    # On récupère tous les rôles pour remplir les listes déroulantes (select)
    roles = Role.objects.all() 
    # --------------------------

    print(f"roles = {roles}")



    # Simulation utilisateur connecté
    user_id_test = 1 
    mes_menus_visibles = MenuAcces.objects.filter(
        user_id=user_id_test, 
        est_visible=True
    ).select_related('menu')
    
    acces_existants = [
        f"{a.user_id}_{a.menu_id}" 
        for a in MenuAcces.objects.filter(est_visible=True)
    ]
    
    return render(request, 'page_utilisateur.html', {
        'users': users,
        'menus': menus,
        'contacts': contacts,
        'roles': roles, # <--- ON AJOUTE LES RÔLES ICI
        'mes_menus_visibles': mes_menus_visibles,
        'acces_existants': acces_existants
    })

# --- ACTIONS SUR LES UTILISATEURS ---

# REMARQUE IMPORTANTE :
######### Dans le FICHIER """"PackageUser/modul_new_user.py/class GestionnaireUtilisateur:"""" se trouvent les FONCTIONS (CRUD) """"def _add_user(self, request):"""" et """"def edit_user(self, request, user_id):"""" et """"def delete_user(self, request, user_id):""""

# app_user > views.py

# REMARQUE IMPORTANTE :
######### Dans le FICHIER """"PackageUser/modul_new_user.py/class GestionnaireUtilisateur:"""" se trouvent les FONCTIONS (CRUD) """"def _add_user(self, request):"""" et """"def edit_user(self, request, user_id):"""" et """"def delete_user(self, request, user_id):""""

def add_user(request):
    """Ajoute un utilisateur via le module externe GestionnaireUtilisateur."""
    if request.method == "POST":
        gestionnaire = GestionnaireUtilisateur()
        # On traite la création (le module gère les validations et le hachage)
        return gestionnaire.creer_un_nouvel_utilisateur(request, "page_utilisateur.html")
            
    return redirect('gestion_globale')

# REMARQUE IMPORTANTE :
######### Dans le FICHIER """"PackageUser/modul_new_user.py/class GestionnaireUtilisateur:"""" se trouvent les FONCTIONS (CRUD) """"def _add_user(self, request):"""" et """"def edit_user(self, request, user_id):"""" et """"def delete_user(self, request, user_id):""""

# app_user > views.py

# REMARQUE IMPORTANTE :
######### Dans le FICHIER """"PackageUser/modul_new_user.py/class GestionnaireUtilisateur:"""" se trouvent les FONCTIONS (CRUD) """"def _add_user(self, request):"""" et """"def edit_user(self, request, user_id):"""" et """"def delete_user(self, request, user_id):""""


# --- GESTION DES PERMISSIONS (MENUS) ---

def update_menus(request):
    """Met à jour les visibilités des menus pour chaque utilisateur."""
    if request.method == "POST":
        users = User.objects.all()
        menus = Menu.objects.all()
        
        for user in users:
            for menu in menus:
                # La clé correspond au 'name' généré dans le template : access_{u.id}_{m.id}
                key = f"access_{user.id}_{menu.id}"
                est_coche = key in request.POST
                
                MenuAcces.objects.update_or_create(
                    user=user, 
                    menu=menu, 
                    defaults={'est_visible': est_coche}
                )
                
        messages.success(request, "Les permissions d'accès aux menus ont été enregistrées.")
        
    return redirect('gestion_globale')


