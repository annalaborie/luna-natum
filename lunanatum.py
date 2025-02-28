import matplotlib.pyplot as plt
import numpy as np


fichiers = ['PN_test.csv','PN_22.csv','PN_21.csv','PN_12.csv','PN_11.csv','PN_02.csv','PN_01.csv']

pleine_lune = ['21/01/2000','19/02/2000','20/03/2000','18/04/2000','18/05/2000','16/06/2000','16/07/2000','15/08/2000','13/09/2000','13/10/2000','11/11/2000','11/12/2000',
'09/01/2001','08/02/2001','09/03/2001','08/04/2001','07/05/2001','06/06/2001','05/07/2001','04/08/2001','02/09/2001','02/10/2001','01/11/2001','30/11/2001','30/12/2001',
'28/01/2002','27/02/2002','28/03/2002','27/04/2002','26/05/2002','24/06/2002','25/07/2002','22/08/2002','21/09/2002','21/10/2002','20/11/2002','19/12/2002',
'18/01/2003','16/02/2003','18/03/2003','16/04/2003','16/05/2003','14/06/2003','13/07/2003','12/08/2003','10/09/2003','10/10/2003','09/11/2003','08/12/2003',
'07/01/2004','06/02/2004','06/03/2004','05/04/2004','04/05/2004','03/06/2004','02/07/2004','31/07/2004','30/08/2004','28/09/2004','28/10/2004','26/11/2004','26/12/2004',
'25/01/2005','24/02/2005','25/03/2005','24/04/2005','23/05/2005','22/06/2005','21/07/2005','19/08/2005','18/09/2005','17/10/2005','16/11/2005','15/12/2005',
'14/01/2006','13/02/2006','14/03/2006','13/04/2006','13/05/2006','11/06/2006','11/07/2006','09/08/2006','07/09/2006','07/10/2006','05/11/2006','05/12/2006',
'03/01/2007','02/02/2007','03/03/2007','02/04/2007','02/05/2007','01/06/2007','30/06/2007','30/07/2007','28/08/2007','26/09/2007','26/10/2007','24/11/2007','24/12/2007',
'22/01/2008','21/02/2008','21/03/2008','20/04/2008','20/05/2008','18/06/2008','18/07/2008','16/08/2008','15/09/2008','14/10/2008','13/11/2008','12/12/2008',
'11/01/2009','09/02/2009','11/03/2009','09/04/2009','09/05/2009','07/06/2009','07/07/2009','06/08/2009','04/09/2009','04/10/2009','02/11/2009','02/12/2009','31/12/2009',
'30/01/2010','28/02/2010','30/03/2010','28/04/2010','27/05/2010','26/06/2010','26/07/2010','24/08/2010','23/09/2010','23/10/2010','21/11/2010','21/12/2010']
    
jours = ["Samedi", "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
annees_bissextiles = [2000, 2004, 2008]
jours_par_mois_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
jours_par_mois_bissextile = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def extraire_et_separer(): #Anna
    """Extrait les dates de naissance des fichiers et les sépare selon le sexe."""
    dates_filles = []
    dates_garcons = []
    
    for fichier in fichiers:
        contenu_fichier = open(fichier, "r", encoding="ISO-8859-1")
        chaine = contenu_fichier.read()
        date = None  
        for i in range(len(chaine)-1):
            if chaine[i] == '\n':
                date = chaine[i+1:i+11]
                genre = chaine[i+12]
                if genre == "F":
                    dates_filles.append(date)
                elif genre == "G":
                    dates_garcons.append(date)
        contenu_fichier.close()
    
    return dates_filles, dates_garcons

filles, garcons = extraire_et_separer()
liste_date_original = (filles) + (garcons)

def lune(liste_date): # Louane et Anna
    
    dico_date = {}
    
    for date in liste_date:
        annee = int(date[6:10])
        if 2000 <= annee <= 2010:
            dico_date[date] = jourPasse(date)
        
    return dico_date


def jourPasse(date_in): # Anna et Louane
    jours_passe = 0
    date = date_in
    while date not in pleine_lune :
        mois = int(date[3:5])
        jour = int(date[0:2])
        annee = int(date[6:10])
             
        jours_passe +=1  
        jour -= 1
        jour_str =""
        mois_str=""
        
        if annee in annees_bissextiles:
            jours_par_mois = jours_par_mois_bissextile
        else:
            jours_par_mois = jours_par_mois_normal
        
        if jour < 1:  
            mois -= 1
            if mois < 1:  
                mois = 12
                annee -= 1
            jour = jours_par_mois[mois - 1]
                       
        if jour < 10:
            jour_str = '0' + str(jour)
        else:
            jour_str = str(jour)

        if mois < 10:
            mois_str = '0' + str(mois)
        else:
            mois_str = str(mois)

        date = jour_str + '/' + mois_str + '/' + str(annee)
        if annee < 2000 or annee > 2010:
            print("Pas de pleine lune en 2000:",date_in)
            return 0

    return jours_passe



def compte_naissances_lune(liste_dates): # Anna
    """Cette fonction utilise la fonction `lune` pour compter le nombre de naissances pour chaque jour avant la pleine lune."""    
    dico_date = lune(liste_dates)  
    resultat = {}
        
    for date, jours_passe in dico_date.items():
        if jours_passe in resultat:
            resultat[jours_passe] += 1
        else:
            resultat[jours_passe] = 1
    
    return resultat


def jour_de_la_smn(jour, mois, annee):  ## Anais
    if annee < 2000 or annee > 2010:
        return "Année invalide"
    
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

def compte_naissances(liste_dates):  # Anais
    
    """Cette fonction prend en argument le fichier, utilise `extraire_dates` pour obtenir la liste des dates,
    puis utilise `compter_jours` pour obtenir la liste des jours de la semaine et renvoie un dictionnaire des jours et de leur nombre d'occurrences."""
    
    liste_jours = compter_jours(liste_dates)
    
    resultat = {}                 # Créer un dictionnaire vide pour stocker les résultats
    for jour in liste_jours:            # Parcourir la liste des jours
        if jour in resultat:      # Si le jour est déjà dans le dictionnaire, on ajoute 1
            resultat[jour] += 1
        else:                     # Sinon, on ajoute le jour avec une valeur de 1
            resultat[jour] = 1
    ordre_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]   # Trier le dictionnaire par ordre des jours de la semaine
    resultat_trie = {jour: resultat[jour] for jour in ordre_jours if jour in resultat}

    return resultat_trie

def genre (liste_dates) : # Anna
    
    """" Compte le nombre de naissances avant la pleine lune separement pour les filles te les garcons."""
    
    filles, garcons = extraire_et_separer()
    
    print('Liste des naissances filles par rapport à la pleine lune', compte_naissances_lune(filles))
    print('Liste des naissances garçons par rapport à la pleine lune', compte_naissances_lune(garcons))
    
    return compte_naissances(filles), compte_naissances (garcons)


def graph_naissances (): # Anna

    liste_jours = compter_jours(liste_date_original)
    repartition_jours = compte_naissances(liste_date_original)

    jours1 = list(repartition_jours.keys())  
    occurences = list(repartition_jours.values())  
    
    x = np.arange(len(jours1))
    width = 0.5  

    fig, ax = plt.subplots(layout='constrained')
    
    rects = ax.bar(x, occurences, width, label="Occurrences des jours",color='crimson',)
    ax.bar_label(rects, padding=3)
    
    ax.set_ylabel('Naissances')
    ax.set_title('Nombre de naissances par jour de la semaine')
    ax.set_xticks(x)
    ax.set_xticklabels(jours1)
    
    plt.show()


def graph_naissances_genre():  # Anna
    filles, garcons = extraire_et_separer()
    resultat_filles = compte_naissances_lune(filles)
    resultat_garcons = compte_naissances_lune(garcons)
    
    jours1 = list(resultat_filles.keys()) 
    
    occurences_filles = list(resultat_filles.values())  
    occurences_garcons = list(resultat_garcons.values())
   
   
    x = np.arange(len(jours1))
    width = 0.4  
       
    fig, ax = plt.subplots(figsize=(12, 6), layout='constrained')
    
    rects1 = ax.bar(x - width/2, occurences_filles, width, color='firebrick', label="Filles")
    rects2 = ax.bar(x + width/2, occurences_garcons, width, color='seagreen', label="Garçons")
    
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    
    ax.set_ylabel('Naissances')
    ax.set_title('Nombre de naissances par jour avant la pleine lune')
    ax.set_xticks(x)
    ax.set_xticklabels(jours1) 
    ax.legend()
    
    plt.show()


