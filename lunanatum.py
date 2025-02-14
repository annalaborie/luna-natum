def extraire_dates(fichier): # Anna
    liste_dates = []
    contenu_fichier = open(fichier, "r",encoding='utf-8')
    chaine = contenu_fichier.read()
    for i in range(len(chaine)-1):
        if chaine[i] == '\n':
            date = chaine[i+1:i+11]
            liste_dates.append(date)
    contenu_fichier.close()
    return liste_dates

def jour_de_la_smn(jour, mois, annee):  ## Anais
    if annee < 2000 or annee > 2010:
        return "Année invalide"
    
    jours = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    annees_bissextiles = [2000, 2004, 2008]
    jours_par_mois_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    jours_par_mois_bissextile = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if annee in annees_bissextiles:
        jours_par_mois = jours_par_mois_bissextile
    else:
        jours_par_mois = jours_par_mois_normal
    
    total_jours = 0
        
    for an in range(2000, annee):
        if an in annees_bissextiles:
            total_jours += 366
        else:
            total_jours += 365
    
    for m in range(mois - 1):  
        total_jours += jours_par_mois[m]
    total_jours += jour - 1
 
    jour_debut = 0  
     
    jour_semaine = jour_debut
    for i in range(total_jours):
        jour_semaine += 1
        if jour_semaine == 7:
            jour_semaine = 0
    
    return jours[jour_semaine]

def compter_jours(liste_dates):  # Mariia
    
    """Cette fonction prend en argument une liste de dates et renvoie une liste des jours de la semaine correspondants."""
    
    jours_de_la_semaine = []

    for date in liste_dates:
        mois = int(date[3:5])
        jour = int(date[0:2])
        annee = int(date[6:])
        jour_semaine = jour_de_la_smn(jour, mois, annee)
        jours_de_la_semaine.append(jour_semaine)

    return jours_de_la_semaine

def compte_naissances(fichier):  # Anais
    
    """Cette fonction prend en argument le fichier, utilise `extraire_dates` pour obtenir la liste des dates,
    puis utilise `compter_jours` pour obtenir la liste des jours de la semaine et renvoie un dictionnaire des jours et de leur nombre d'occurrences."""
    
    
    liste_dates = extraire_dates(fichier) 
    liste_jours = compter_jours(liste_dates)
    
    resultat = {}                 # Créer un dictionnaire vide pour stocker les résultats
    for jour in liste_jours:            # Parcourir la liste des jours
        if jour in resultat:      # Si le jour est déjà dans le dictionnaire, on ajoute 1
            resultat[jour] += 1
        else:                     # Sinon, on ajoute le jour avec une valeur de 1
            resultat[jour] = 1
    ordre_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]       # Trier le dictionnaire par ordre des jours de la semaine
    resultat_trie = {jour: resultat[jour] for jour in ordre_jours if jour in resultat}

    return resultat_trie


import matplotlib.pyplot as plt
import numpy as np

def graph_naissances (fichier): # Anna
    liste_dates = extraire_dates(fichier)
    liste_jours = compter_jours(liste_dates)
    repartition_jours = compte_naissances(fichier)
    
#  species = (jour de la semaine)
#penguin_means = {
#    'Filles': (???),
#    'Garçons': (???)'
#}
    jours = list(repartition_jours.keys())  
    occurences = list(repartition_jours.values())  
    
    x = np.arange(len(jours))
    width = 0.5  

    fig, ax = plt.subplots(layout='constrained')
    
    rects = ax.bar(x, occurences, width, label="Occurrences des jours")
    ax.bar_label(rects, padding=3)
    
    ax.set_ylabel('Naissances')
    ax.set_title('Nombre de naissances par jour de la semaine')
    ax.set_xticks(x)
    ax.set_xticklabels(jours)
    
    plt.show()


