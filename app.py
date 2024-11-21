import requests

# Constantes

NOMBRE_LIVRES = 10 # Nombre de livres à afficher, la valeur peut être modifiée

# URL de l'API OpenLibrary
URL = "https://openlibrary.org/search.json?q=cybersecurity"

def recuperer_donnees_livres(api_url):
    """
    Récupère les données des livres à partir de l'API OpenLibrary

    :param api_url: URL de l'API
    :type api_url: str
    :return: liste des livres sinon une liste vide
    :rtype: list
    """
    try:
        reponse = requests.get(api_url)
        reponse.raise_for_status()  # Lève une exception en cas d'erreur HTTP par exemple 404, 500 ...
        return reponse.json().get("docs", [])
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return []


def trier_livres_par_annee(liste_livres):
    """
    Trie les livres par année de publication en ordre décroissant

    :param liste_livres: liste des livres
    :type liste_livres: list
    :return: liste des livres triés
    :rtype: list
    """
    return sorted(liste_livres, key=lambda x: x.get("first_publish_year", float("-inf")), reverse=True)


def afficher_info_livre(livre_detail):
    """
    Affiche les informations d'un livre de manière lisible

    :param livre_detail: détails du livre
    :type livre_detail: dict
    """
    # Récupération des informations
    titre = livre_detail.get("title", "Titre inconnu")
    auteurs = livre_detail.get("author_name", ["Auteur inconnu"])
    annee = livre_detail.get("first_publish_year", "Année inconnue")
    editeurs = ", ".join(livre_detail.get("publisher", ["Éditeur inconnu"]))

    # Affichage
    print("*" * 70)
    print(f"Titre : {titre}")
    print(f"Auteur(s) : {', '.join(auteurs)}")
    print(f"Année de publication : {annee}")
    print(f"Éditeur(s) : {editeurs}")
    print("*" * 70)
    print()

# Fonction principale !
def main():
    print("\nRecherche de livres sur la cybersécurité en cours... ")

    # Récupération et tri des livres
    livres = recuperer_donnees_livres(URL)
    livres_tries = trier_livres_par_annee(livres)

    # Affichage des livres
    if livres_tries:
        print("\n" + "*" * 70)
        print("les 10 livres les plus récents ordonnés par date de publication".center(70))
        print("*" * 70)
        print()
        for livre in livres_tries[:NOMBRE_LIVRES]:
            afficher_info_livre(livre)
    else:
        print("Aucun livre n'a pu être récupéré.")


if __name__ == "__main__":
    main()