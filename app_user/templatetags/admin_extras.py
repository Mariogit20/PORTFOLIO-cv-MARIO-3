# # # # from django import template

# # # # register = template.Library()

# # # # @register.simple_tag
# # # # def check_access(user_id, menu_id, acces_existants):
# # # #     """
# # # #     Vérifie si la clé 'userID_menuID' est présente dans la liste fournie.
# # # #     """
# # # #     key = f"{user_id}_{menu_id}"
# # # #     return key in acces_existants


# # # from django import template

# # # register = template.Library()

# # # @register.simple_tag
# # # def check_access(user_id, menu_id, acces_map):
# # #     """
# # #     Vérifie si menu_id est dans la liste associée à user_id dans le dictionnaire acces_map.
# # #     """
# # #     # On récupère la liste des menus pour cet utilisateur (vide si aucune permission)
# # #     user_perms = acces_map.get(user_id, [])
# # #     return menu_id in user_perms



# from django import template

# register = template.Library()

# # # @register.simple_tag
# # # def check_access(user_id, menu_id, acces_map):
# # #     """
# # #     Vérifie si menu_id est dans la liste associée à user_id dans le dictionnaire acces_map.
# # #     """
# # #     # On récupère la liste des menus pour cet utilisateur (vide si aucune permission)
# # #     user_perms = acces_map.get(user_id, [])
# # #     return menu_id in user_perms


# # # admin_extras.py
# # @register.simple_tag
# # def check_access(user_id, menu_id, acces_map):
# #     # Si acces_map est une chaîne ici, c'est que le template envoie mal les données
# #     if isinstance(acces_map, str):
# #         return False  # Sécurité pour éviter le crash
    
# #     user_perms = acces_map.get(user_id, [])
# #     return menu_id in user_perms


# @register.simple_tag
# def check_access(user_id, menu_id, acces_list):
#     # On recrée la clé '1_1' pour vérifier si elle est dans ['1_1', '1_3', ...]
#     if not acces_list:
#         return False
#     key = f"{user_id}_{menu_id}"
#     return key in acces_list


from django import template

register = template.Library()

@register.simple_tag
def check_access(user_id, menu_id, acces_existants):
    """
    Vérifie si la combinaison 'userID_menuID' est dans la liste des accès.
    """
    # Sécurité : si la liste est vide ou n'est pas une liste, on renvoie False
    if not isinstance(acces_existants, list):
        return False
    
    # On crée la clé au format "1_3" (comme dans votre debug log)
    key = f"{user_id}_{menu_id}"
    
    # On vérifie la présence dans la liste
    return key in acces_existants






# 2. Filtres personnalisés (templatetags/admin_extras.py)

# Ce fichier est crucial pour que votre template puisse lire facilement le dictionnaire des accès.

# from django import template
# register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Permet d'accéder à un dictionnaire dans un template : dict|get_item:key"""
    return dictionary.get(key, [])


