import requests

def recuperer_donnees_livres(api_url):
    """
    Cette fonction récupère les données des livres à partir de l'API OpenLibrary.
    :param api_url: URL de l'API
    :type api_url: str
    :return: liste des livres sinon une liste vide
    :rtype: list
    """
    reponse = requests.get(api_url)

    if reponse.status_code == 200:
        return reponse.json().get("docs", [])
    else:
        print(f"Erreur : {reponse.status_code}")
        return []


def trier_livres_par_annee(liste_livres):
    """
    Cette fonction trie les livres par année de publication.
    :param liste_livres: liste des livres
    :type liste_livres: list
    :return: liste des livres triés
    :rtype: list
    """
    return sorted(liste_livres, key=lambda x: x.get("first_publish_year", float("inf")))


def afficher_info_livre(livre_detail):
    """
    Cette fonction affiche les informations d'un livre
    :param livre_detail: détails du livre
    :type livre_detail: dict
    """
    # On récupère le titre, mais si on ne le trouve pas, on met "Titre inconnu"
    # On fait de même pour auteur, année, éditeur et sujets
    titre = livre_detail.get("title", "Titre inconnu")
    auteur = ", ".join(livre_detail.get("author_name", ["Auteur inconnu"]))
    annee = livre_detail.get("first_publish_year", "Année inconnue")
    editeur = ", ".join(livre_detail.get("publisher", ["Éditeur inconnu"]))
    sujets = ", ".join(livre_detail.get("subject", ["Aucun sujet disponible"]))

    # Affichage des informations
    print(f"Titre : {titre}")
    print(f"Auteur(s) : {auteur}")
    print(f"Année de publication : {annee}")
    print(f"Éditeur(s) : {editeur}")
    print(f"Sujets : {sujets}\n")


# URL de l'API OpenLibrary
url = "https://openlibrary.org/search.json?q=cybersecurity"

# Recupération des données des livres (appel à la fonction recuperer_donnees_livres)
livres = recuperer_donnees_livres(url)

# Tri des livres par année (appel à la fonction trier_livres_par_annee)
livres_tries = trier_livres_par_annee(livres)

# Affichage des informations des 10 premiers livres
for livre in livres_tries[:10]:
    afficher_info_livre(livre) # on appelle la fonction afficher_info_livre pour chaque livre