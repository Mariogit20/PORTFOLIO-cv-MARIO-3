from django.urls import path
from .views import *
urlpatterns = [


# Votre page publique (Vue par les visiteurs)
    # Assurez-vous d'avoir créé la fonction 'page_publique' dans views.py
    path('', aff_acceuil_PAGE_PUBLIQUE_Vue_par_les_VISITEURS,name="name_acceuil"),       
    path('index.html', aff_acceuil_PAGE_PUBLIQUE_Vue_par_les_VISITEURS,name="name_acceuil"),          
#    Mon Espace Administration   
#    Mon Espace Administration   
#    Mon Espace Administration   
#    Mon Espace Administration    
# Votre Dashboard personnalisé (Sécurisé dans views.py)
path('dashboard', page_Mon_Espace_Administration, name='dashboard_admin'),
    


# PAGE de CAMIONS DE TRANSPORT DE MARCHANDISES
path('Page_CAMIONS_DE_TRANSPORT_DE_MARCHANDISES', Fonction_Page_CAMIONS_DE_TRANSPORT_DE_MARCHANDISES, name='name_Page_CAMIONS_DE_TRANSPORT_DE_MARCHANDISES'),




# FORMULAIRE d'un    ENVOI d'un EMAIL    en javascript


# https://gemini.google.com/app/50f984f5e7992921?hl=fr
# https://gemini.google.com/app/50f984f5e7992921?hl=fr
# https://gemini.google.com/app/2b0ac21fa009d2d9?hl=fr
# https://gemini.google.com/app/50f984f5e7992921?hl=fr
# https://gemini.google.com/app/50f984f5e7992921?hl=fr



# Pourquoi séparer l'ancre du nom du fichier ?

# Le schéma suivant montre comment Django traite votre demande :

#     Le Navigateur demande une URL.

#     Django exécute la fonction dans views.py.

#     Django cherche le fichier template (sans l'ancre car le système de fichier ne la reconnaît pas).

#     Django renvoie le HTML au navigateur.

#     Le Navigateur reçoit la page et, voyant #email_JAVASCRIPT dans son URL, fait défiler la page automatiquement.

# Souhaitez-vous que je vous aide à écrire le script JavaScript pour récupérer les données du formulaire et envoyer l'email ?


# Comment l'utilisateur arrive sur l'ancre ? Dans vos autres pages HTML (par exemple votre menu), votre lien doit ressembler à ceci :

path('Page_email_Javascript', Fonction_Page_email_Javascript, name='name_Page_email_Javascript'),

    # href="index.html#accueil"
path('Page_accueil_section_Accueil', Fonction_Page_accueil_section_Accueil, name='name_Page_accueil_section_Accueil'),

    # href="index.html#projets"
path('Page_accueil_section_projets', Fonction_Page_accueil_section_projets, name='name_Page_accueil_section_projets'),

    # href="index.html#temoignages"
path('Page_accueil_section_temoignages', Fonction_Page_accueil_section_temoignages, name='name_Page_accueil_section_temoignages'),

    # href="index.html#a-propos"
path('Page_accueil_section_a_propos', Fonction_Page_accueil_section_a_propos, name='name_Page_accueil_section_a_propos'),

    # href="index.html#contact"
path('Page_accueil_section_contact', Fonction_Page_accueil_section_contact, name='name_Page_accueil_section_contact'),
]
