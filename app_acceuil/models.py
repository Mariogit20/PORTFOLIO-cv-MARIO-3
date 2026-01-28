    





# //        window.location.href = "/";       //  Garde l'historique ?  Oui      //  Navigation standard entre les pages.



# // On ""RECHARGE COMPLETEMENT"" la ""PAGE D'ACCUEIL"" nommé ""index.html"" afin de """"FAIRE APPARAITRE"""" les """"IMAGES"""" contenues dans le FICHIER """"index.html"""" :::::::::::::::::::::::::

# ///// window.location.href = "/"       //  Garde l'historique ?  Oui      //  Navigation standard entre les pages.








# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c   


# https://gemini.google.com/app?hl=fr
# https://gemini.google.com/app?hl=fr
# https://gemini.google.com/app?hl=fr 
    




# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e



        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e      





from django.db import models
import re

# --- FONCTION UTILITAIRE POUR LE NETTOYAGE ---
def nettoyer_espaces(texte):
    if texte:
        return re.sub(r'\s+', ' ', texte).strip()
    return texte



# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c





# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e
# https://gemini.google.com/app/1332cca0d76a0b1e


        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e
        # https://gemini.google.com/app/1332cca0d76a0b1e      






# 1. TEMOIGNAGES
class Projetscards(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=False)
    images = models.ImageField(upload_to="static/images/", null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    est_visible = models.BooleanField(default=True, verbose_name="Afficher sur le site")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages Clients"
        ordering = ['-created_at']

    def clean(self):
        self.nom = nettoyer_espaces(self.nom)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom if self.nom else f"Témoignage {self.id}"




# 2. SPECIALITES
class Projetsfirstspeciality(models.Model):
    images = models.ImageField(upload_to="static/images/", null=True, blank=False)
    description_speciality = models.TextField(null=True, blank=False)
    est_visible = models.BooleanField(default=True, verbose_name="Afficher sur le site")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        # Nom de l'élément individuel
        verbose_name = "Ma Photo de Spécialisation"
        # Nom de la section dans le menu de gauche de l'admin
        verbose_name_plural = "Mes Photos de Spécialisation"
        ordering = ['-created_at']

    def __str__(self):
        # Affiche un extrait du texte dans la liste pour s'y retrouver
        return self.description_speciality[:50] if self.description_speciality else f"Spécialité {self.id}"



# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c
# https://gemini.google.com/app/b83bdb7ebec35a6c

# 💡 Rappel pour la mise en ligne

# Pensez à exécuter les commandes habituelles pour que Django valide ces nouveaux noms :

#     python manage.py makemigrations

#     python manage.py migrate


# 3. REALISATIONS
class Projetmesrealisations(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=False)
    images = models.ImageField(upload_to="static/images/", null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    est_visible = models.BooleanField(default=True, verbose_name="Afficher sur le site")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        # Nom affiché dans le menu de l'admin
        verbose_name = "Réalisation"
        # Nom affiché au pluriel
        verbose_name_plural = "Mes Réalisations"
        # Tri : les plus récents apparaissent en premier
        ordering = ['-created_at']

    def clean(self):
        self.nom = nettoyer_espaces(self.nom)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom if self.nom else f"Projet Réalisé {self.id}"




# 4. PHOTO DE PROFIL
class Projetphotodeprofil(models.Model):
    images = models.ImageField(upload_to="static/images/", null=True, blank=False)
    est_visible = models.BooleanField(default=True, verbose_name="Afficher cette photo")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Photo de profil"
        verbose_name_plural = "Ma Photo de profil"
        # Même s'il n'y en a qu'une (Singleton), on garde une cohérence de tri
        ordering = ['-created_at']

    def __str__(self):
        status = "Visible" if self.est_visible else "Cachée"
        return f"Photo de profil du {self.created_at.strftime('%d/%m/%Y')} ({status})"


# 5. A PROPOS
class ProjetAproposDeMoi(models.Model):
    description = models.TextField(null=True, blank=False)
    est_visible = models.BooleanField(default=True, verbose_name="Afficher la section")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "A propos de Moi"
        verbose_name_plural = "A propos de Moi"
        ordering = ['-created_at']

    def __str__(self):
        status = "Visible" if self.est_visible else "Cachée"        
        # Pour que ce soit lisible dans l'admin même sans champ 'nom'
        return f"Mon profil (créé le {self.created_at.strftime('%d/%m/%Y')} ({status})"

# 6. COMPETENCES CLES (Avec Unicité et Nettoyage)
class MesCompetencesCles(models.Model):
    nom = models.CharField(
        max_length=100, 
        unique=True, 
        null=True, 
        blank=False,
        help_text="Le nom de la compétence (ex: Python)"
    )
    est_visible = models.BooleanField(default=True, verbose_name="Afficher sur le site")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Compétence clé"
        verbose_name_plural = "Mes compétences clés"
        ordering = ['-created_at']

    def clean(self):
        self.nom = nettoyer_espaces(self.nom)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom if self.nom else f"Compétence {self.id}"
    
    

class ReseauSocial(models.Model):
    NOM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('facebook', 'Facebook'),
        ('twitter','X (Twitter)'),
        ('instagram', 'Instagram'),        
    ]
    nom = models.CharField(max_length=20, choices=NOM_CHOICES, unique=True)
    url = models.URLField(max_length=200)
    est_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Réseau Social"
        verbose_name_plural = "Réseaux Sociaux"

    def __str__(self):
        return self.nom


        