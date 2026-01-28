



from django.db import models



# https://gemini.google.com/app/4087d09848fdd4b6
# https://gemini.google.com/app/c25ec29c52442407
# https://gemini.google.com/app/822028a316d61568




class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom


# //        window.location.href = "/";       //  Garde l'historique ?  Oui      //  Navigation standard entre les pages.



# // On ""RECHARGE COMPLETEMENT"" la ""PAGE D'ACCUEIL"" nommé ""index.html"" afin de """"FAIRE APPARAITRE"""" les """"IMAGES"""" contenues dans le FICHIER """"index.html"""" :::::::::::::::::::::::::

# ///// window.location.href = "/"       //  Garde l'historique ?  Oui      //  Navigation standard entre les pages.








# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e



        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e      




# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397
# https://gemini.google.com/app/bbba657c1b185397



# https://gemini.google.com/app/e90aa1b5c8659267
# https://gemini.google.com/app/e90aa1b5c8659267
# https://gemini.google.com/app/e90aa1b5c8659267
# https://gemini.google.com/app/e90aa1b5c8659267




# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494




# page_inscription.html

# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494
# https://gemini.google.com/app/f7b714a644fad494 





# https://gemini.google.com/app/cbb617324b1498ce
# https://gemini.google.com/app/cbb617324b1498ce
# https://gemini.google.com/app/cbb617324b1498ce
# https://gemini.google.com/app/cbb617324b1498ce
# https://gemini.google.com/app/cbb617324b1498ce





# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e



        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e      








# # Étapes à suivre pour appliquer le changement

# # Une fois que vous avez modifié votre fichier models.py, vous devez impérativement mettre à jour votre base de données :

# #     Créer la migration : python manage.py makemigrations

# #     Appliquer la migration : python manage.py migrate

# #     [!CAUTION] Attention : Si votre base de données contient déjà des doublons (deux utilisateurs avec le même email), la migration va échouer. Vous devrez d'abord supprimer ou modifier les doublons manuellement avant de lancer migrate.
    


# https://gemini.google.com/app/f1c52fba06c87797
# https://gemini.google.com/app/f1c52fba06c87797    
    

# 1. MODÈLE DES RÔLES
class Role(models.Model):
    nom_role = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom_role

# 2. MODÈLE DES UTILISATEURS
class User(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) # Stocke le hash
    # Relation ForeignKey vers Role
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="utilisateurs")


    def __str__(self):
        return f"{self.nom} ({self.role.nom_role})"
    
    
    
                