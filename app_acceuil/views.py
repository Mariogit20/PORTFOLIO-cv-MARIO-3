from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (
    Projetscards, Projetsfirstspeciality, Projetmesrealisations, 
    Projetphotodeprofil, ProjetAproposDeMoi, MesCompetencesCles, ReseauSocial
)
    
# Importations des modèles
from app_user.models import MenuAcces




# //        window.location.href = "/";       //  Garde l'historique ?  Oui      //  Navigation standard entre les pages.



# // On ""RECHARGE COMPLETEMENT"" la ""PAGE D'ACCUEIL"" nommé ""index.html"" afin de """"FAIRE APPARAITRE"""" les """"IMAGES"""" contenues dans le FICHIER """"index.html"""" :::::::::::::::::::::::::

# ///// window.location.href = "/"       //  Garde l'historique ?  Oui      //  Navigation standard entre les pages.








# https://gemini.google.com/app/3bd97af244610ffd?hl=fr
# https://gemini.google.com/app/3bd97af244610ffd?hl=fr
# https://gemini.google.com/app/3bd97af244610ffd?hl=fr
# https://gemini.google.com/app/3bd97af244610ffd?hl=fr
# https://gemini.google.com/app/3bd97af244610ffd?hl=fr





# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397






# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e






# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e









# =========================================================================
# 1. VUE PUBLIQUE (Portfolio)
# =========================================================================
def aff_acceuil_PAGE_PUBLIQUE_Vue_par_les_VISITEURS(request):
    """ Filtre et affiche uniquement les éléments marqués comme visibles """
    temoignages = Projetscards.objects.filter(est_visible=True)
    specialites = Projetsfirstspeciality.objects.filter(est_visible=True)
    realisations = Projetmesrealisations.objects.filter(est_visible=True)
    mescompetencescles = MesCompetencesCles.objects.filter(est_visible=True)
    reseaux = ReseauSocial.objects.filter(est_visible=True)

    photodeprofil = Projetphotodeprofil.objects.filter(est_visible=True).first()
    aproposdemoi = ProjetAproposDeMoi.objects.filter(est_visible=True).first()



        
    # Logique des menus (Simulation utilisateur ID 1 pour la session de test)
    # Logique des menus (Simulation ID 1)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)
    # Récupérer les menus à afficher pour l'utilisateur connecté (ex: ID 1 pour test)        
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )
    # user_id_test = 3     # TABLE ====>      app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )
        

    

    # https://gemini.google.com/app/1b31b1ccfe391648
    # https://gemini.google.com/app/1b31b1ccfe391648
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )                                 
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )
    # user_id_test = 3     # TABLE ====>      app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )
    # Récupérer le dictionnaire 'user' (retourne None s'il n'existe pas)
    user_session_data = request.session.get('user')

    if user_session_data:
        # Extraire l'id du dictionnaire
        user_id_test = user_session_data.get('id')
        print(f"ID récupéré depuis la session : {user_id_test}")
    else:
        # Valeur par défaut ou redirection si pas de session
        user_id_test = 1
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )       
    # user_id_test = 1     # TABLE ====>        app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )                                                
    

    
    
    # user_id_test = 1     # TABLE ====>      app_user_menuacces        ,       COLONNE =======>      user_id      (Deuxième CLEF COMPOSEE !!!!!!!!!!!!!!!!!!!!! )    
    mes_menus_visibles = MenuAcces.objects.filter(user_id=user_id_test, est_visible=True).select_related('menu')
    
    print(f"mes_menus_visibles = {mes_menus_visibles}")
     

    contenu = {
        "TEMOIGNAGES_des_PERSONNES_cards": temoignages,
        "EXISTENCE_de_TEMOIGNAGES": temoignages.exists(),
        "AFFICHER_la_PREMIERE_SPECIAISATION": specialites,
        "EXISTENCE_de_PREMIERE_SPECIAISATION": specialites.exists(),
        "AFFICHER_les_REALISATIONS_PERSONNELLES": realisations,
        "EXISTENCE_de_REALISATIONS_PERSONNELLES": realisations.exists(),
        "AFFICHER_la_PHOTO_DE_PROFIL": photodeprofil,
        "A_PROPOS_DE_MOI": aproposdemoi,
        "Mes_Competences_Cles": mescompetencescles,
        "Mes_Reseaux": reseaux, 
        "mes_menus_visibles": mes_menus_visibles,
    }
    return render(request, "index.html", contenu)





# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e


        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e        





# =========================================================================
# 2. DASHBOARD D'ADMINISTRATION
# =========================================================================
def page_Mon_Espace_Administration(request):
    # Récupération des données existantes (pour affichage dans les formulaires)
    photo_profil = Projetphotodeprofil.objects.first()
    a_propos = ProjetAproposDeMoi.objects.first()
    specialite = Projetsfirstspeciality.objects.first()
    
    print(f"page_Mon_Espace_Administration")
        
        
        
    
    
    

    # DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
    #     DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
    #         DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
    #             DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
    #                 DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
    #                     DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
    #                         DEBUT =============>    ⚠️ Accès refusé : vous devez être Administrateur.     ::::::::::::::::::::::::
        
    # 1. On récupère les données de l'utilisateur (on utilise .get pour éviter une erreur si 'user' n'existe pas)
    user_data = request.session.get('user')

    # https://gemini.google.com/app/5a9a859ff2a2f94e
    # https://gemini.google.com/app/5a9a859ff2a2f94e
    # https://gemini.google.com/app/5a9a859ff2a2f94e

    # Pourquoi utiliser or au lieu de and ici ?

    # En programmation, quand on veut "bloquer" l'accès, on utilise souvent la logique suivante : "Si tu n'as pas de badge OU si ton badge n'est pas le bon, tu sors".

    # En programmation, quand on veut "bloquer" l'accès, on utilise souvent la logique suivante : "Si tu n'as pas de badge OU si ton badge n'est pas le bon, tu sors".

    # En programmation, quand on veut "bloquer" l'accès, on utilise souvent la logique suivante : "Si tu n'as pas de badge OU si ton badge n'est pas le bon, tu sors".

    # En programmation, quand on veut "bloquer" l'accès, on utilise souvent la logique suivante : "Si tu n'as pas de badge OU si ton badge n'est pas le bon, tu sors".

    # En programmation, quand on veut "bloquer" l'accès, on utilise souvent la logique suivante : "Si tu n'as pas de badge OU si ton badge n'est pas le bon, tu sors".

    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'
    # 2. On vérifie : si la session n'existe pas OU si le rôle n'est pas 'Administrateur'                                    

    #     # Redirection vers l'accueil si l'une des deux conditions est vraie
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }
    #     # TABLE """"""""app_contact_role"""""""" , COLONNE """"""""nom_role"""""""" , VALEUR = { Administrateur , Moderateur , Utilisateur , Responsable de Saisie }


    # https://gemini.google.com/app/57bb0c3daec258cd
    # https://gemini.google.com/app/57bb0c3daec258cd
    # https://gemini.google.com/app/57bb0c3daec258cd
    # https://gemini.google.com/app/57bb0c3daec258cd
    # https://gemini.google.com/app/57bb0c3daec258cd

    if not user_data or (user_data.get('role') != 'Administrateur' and user_data.get('role') != 'Moderateur'):
        messages.error(request, "Accès refusé : vous devez être Administrateur ou Modérateur.")
        return redirect('name_acceuil')

    # 3. Si on arrive ici, l'utilisateur est connecté ET c'est un admin
    # Le reste de ton code s'exécute normalement...    

    # FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    #     FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    #         FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    #             FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    #                 FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    #                     FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    #                         FIN =============>    ⚠️ Accès refusé : vous devez être Administrateur.     !!!!!!!!!!!!!!!!!!!!!!!!
    
    
    
    
    

    else:                                  # L'UTILISATEUR   est   """""CONNECTE"""""    avec son   """""EMAIL"""""  et  son   """""MOT DE PASSE""""" 
        # On vérifie si l'utilisateur est présent :::::::::::::
        
        # On récupère le dictionnaire
        user_data = request.session['user']     #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""

        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e        
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        # On accède aux valeurs spécifiques
        user_id = user_data['id']     #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e                
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        nom_utilisateur = user_data['nom']     #  LECTURE des """""VARIABLES SESSIONS"""""      #  VARIABLES SESSIONS ==========>         """""request.session['user'] = {'id': nouvel_utilisateur.id, 'nom': nouvel_utilisateur.nom}"""""       # =========>    Ces   """""VARIABLES SESSIONS"""""   sont """""PRESENTES""""" dans la    FONCTION     """""def index_inscription_view(request):"""""      dans le    FICHIER     """""app_contact/views.py"""""
        
        print(f"user_id de l'UTILISATEUR CONNECTE = {user_id}")
        
        print(f"nom_utilisateur de l'UTILISATEUR CONNECTE = {nom_utilisateur}")
        
        
        
        

    if request.method == 'POST':
        
        # --- PHOTO DE PROFIL (SWITCH AUTO) ---
        if 'btn_visibilite_photo_auto' in request.POST:
            vis = 'est_visible' in request.POST
            if photo_profil:
                photo_profil.est_visible = vis
                photo_profil.save()
            messages.info(request, "Visibilité de la photo mise à jour.")

        # --- PHOTO DE PROFIL (UPLOAD/UPDATE) ---
        elif 'btn_photo' in request.POST:
            img = request.FILES.get('images')
            if photo_profil:
                if img: photo_profil.images = img
                photo_profil.save()
            else:
                Projetphotodeprofil.objects.create(images=img, est_visible=True)
            messages.success(request, "Photo enregistrée.")

        elif 'btn_supprimer_photo' in request.POST:
            if photo_profil: photo_profil.delete()
            messages.warning(request, "Photo supprimée.")

        # --- À PROPOS (BIO - SWITCH AUTO) ---
        elif 'btn_visibilite_bio_auto' in request.POST:
            vis = 'est_visible_bio' in request.POST
            if a_propos:
                a_propos.est_visible = vis
                a_propos.save()

            
            print(f"vis = {vis}")    # vis = False    # vis = True
                
                
            messages.info(request, "Visibilité de la bio mise à jour.")

        # --- À PROPOS (BIO - TEXTE) ---
        elif 'btn_apropos' in request.POST:
            description = request.POST.get('description')
            if a_propos:
                a_propos.description = description
                a_propos.save()
            else:
                ProjetAproposDeMoi.objects.create(description=description, est_visible=True)
            messages.success(request, "Texte de la bio mis à jour.")

        elif 'btn_supprimer_apropos' in request.POST:
            if a_propos: a_propos.delete()
            messages.error(request, "Texte biographique supprimé.")

        # --- SPÉCIALITÉ ---
        elif 'btn_visibilite_section_spec' in request.POST:
            vis = 'est_visible' in request.POST
            Projetsfirstspeciality.objects.all().update(est_visible=vis)
            messages.info(request, "Visibilité section Spécialité modifiée.")

        elif 'btn_specialite' in request.POST:
            img = request.FILES.get('images')
            desc = request.POST.get('description_speciality')
            if specialite:
                specialite.description_speciality = desc
                if img: specialite.images = img
                specialite.save()
            else:
                Projetsfirstspeciality.objects.create(description_speciality=desc, images=img, est_visible=True)
            messages.success(request, "Détails de la spécialité mis à jour.")

        # --- RÉALISATIONS (PROJETS) ---
        elif 'btn_visibilite_section_real' in request.POST:
            vis = 'est_visible' in request.POST
            Projetmesrealisations.objects.all().update(est_visible=vis)
            messages.info(request, "Section Projets mise à jour.")

        elif 'btn_bascule_vis_real' in request.POST:
            obj = get_object_or_404(Projetmesrealisations, id=request.POST.get('id_realisation'))
            obj.est_visible = not obj.est_visible
            obj.save()

        elif 'btn_ajouter_real' in request.POST:
            Projetmesrealisations.objects.create(
                nom=request.POST.get('nom'),
                description=request.POST.get('description'),
                images=request.FILES.get('images'),
                est_visible=True
            )
            messages.success(request, "Projet ajouté.")

        elif 'btn_modifier_real' in request.POST:
            obj = get_object_or_404(Projetmesrealisations, id=request.POST.get('id_realisation'))
            obj.nom = request.POST.get('nom')
            obj.description = request.POST.get('description')
            if request.FILES.get('images'): obj.images = request.FILES.get('images')
            obj.save()
            messages.info(request, "Projet modifié.")

        elif 'btn_supprimer_real' in request.POST:
            get_object_or_404(Projetmesrealisations, id=request.POST.get('id_realisation')).delete()
            messages.warning(request, "Projet supprimé.")

        # --- TÉMOIGNAGES ---
        elif 'btn_visibilite_section_tem' in request.POST:
            vis = 'est_visible' in request.POST
            Projetscards.objects.all().update(est_visible=vis)

        elif 'btn_bascule_vis_tem' in request.POST:
            obj = get_object_or_404(Projetscards, id=request.POST.get('id_temoignage'))
            obj.est_visible = not obj.est_visible
            obj.save()

        elif 'btn_ajouter_temoignage' in request.POST:
            Projetscards.objects.create(
                nom=request.POST.get('nom'),
                description=request.POST.get('description'),
                images=request.FILES.get('images'),
                est_visible=True
            )
            messages.success(request, "Témoignage ajouté.")

        elif 'btn_supprimer_temoignage' in request.POST:
            get_object_or_404(Projetscards, id=request.POST.get('id_temoignage')).delete()

        # --- COMPÉTENCES ---
        elif 'btn_visibilite_section_comp' in request.POST:
            vis = 'est_visible' in request.POST
            MesCompetencesCles.objects.all().update(est_visible=vis)

        elif 'btn_bascule_vis_comp' in request.POST:
            obj = get_object_or_404(MesCompetencesCles, id=request.POST.get('id_competence'))
            obj.est_visible = not obj.est_visible
            obj.save()

        elif 'btn_ajouter_comp' in request.POST:
            MesCompetencesCles.objects.create(nom=request.POST.get('nom_competence'), est_visible=True)
            messages.success(request, "Compétence ajoutée.")

        elif 'btn_supprimer_comp' in request.POST:
            get_object_or_404(MesCompetencesCles, id=request.POST.get('id_competence')).delete()

        # --- RÉSEAUX SOCIAUX ---
        elif 'btn_visibilite_section_res' in request.POST:
            vis = 'est_visible' in request.POST
            ReseauSocial.objects.all().update(est_visible=vis)

        elif 'btn_reseau' in request.POST:
            ReseauSocial.objects.update_or_create(
                nom=request.POST.get('nom_reseau'),
                defaults={'url': request.POST.get('url_reseau'), 'est_visible': True}
            )
            messages.success(request, "Réseau mis à jour.")

        elif 'btn_supprimer_reseau' in request.POST:
            get_object_or_404(ReseauSocial, id=request.POST.get('id_reseau')).delete()

        # Redirection finale
        return redirect('dashboard_admin')

    # Contexte
    context = {
        'AFFICHER_la_PHOTO_DE_PROFIL': photo_profil,
        'A_PROPOS_DE_MOI': a_propos,
        'SPECIALITE': specialite,
        'AFFICHER_les_REALISATIONS_PERSONNELLES': Projetmesrealisations.objects.all().order_by('-id'),
        'TEMOIGNAGES_des_PERSONNES_cards': Projetscards.objects.all().order_by('-id'),
        'Mes_Competences_Cles': MesCompetencesCles.objects.all().order_by('nom'),
        'Mes_Reseaux': ReseauSocial.objects.all(),
    }
    return render(request, 'page_administration.html', context)

# =========================================================================
# 3. REDIRECTIONS
# =========================================================================
def Fonction_Page_accueil_section_Accueil(request): return redirect('/#accueil')
def Fonction_Page_accueil_section_projets(request): return redirect('/#projets')
def Fonction_Page_accueil_section_temoignages(request): return redirect('/#temoignages')
def Fonction_Page_accueil_section_a_propos(request): return redirect('/#a-propos')
def Fonction_Page_accueil_section_contact(request): return redirect('/#contact')
# def Fonction_Page_email_Javascript(request): return redirect('/#email_JAVASCRIPT')

def Fonction_Page_email_Javascript(request): return render(request, 'email_Javascript.htm')

def Fonction_Page_CAMIONS_DE_TRANSPORT_DE_MARCHANDISES(request): return render(request, 'TransportRoutier_Main.html')