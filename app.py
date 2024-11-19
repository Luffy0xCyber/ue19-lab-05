# On importe la bibliothèque qui nous permet de faire des requêtes web
import requests

# On définit l'adresse web où on va chercher des livres sur la cybersécurité
url = "https://openlibrary.org/search.json?q=cybersecurity"

response = requests.get(url)

# Si le site répond correctement (code 200 = "tout va bien")
if response.status_code == 200:
    # On récupère la liste des livres trouvés
    books = response.json().get("docs", [])

    # On va maintenant trier ces livres du plus ancien au plus récent
    sorted_books = sorted(books, key=lambda x: x.get("first_publish_year", float("inf")))

    # On va afficher les détails des 10 premiers livres triés
    for book in sorted_books[:10]:
        # On récupère le titre, mais si on ne le trouve pas, on met "Titre inconnu"
        title = book.get("title", "Titre inconnu")

        # Pareil pour l'auteur : si plusieurs auteurs, on les sépare par une virgule
        # Si pas d'auteur, on met "Auteur inconnu"
        author = ", ".join(book.get("author_name", ["Auteur inconnu"]))

        # On récupère l'année de publication ou on met "Année inconnue"
        year = book.get("first_publish_year", "Année inconnue")

        # On affiche joliment les informations de chaque livre
        print(f"Titre : {title}\nAuteur(s) : {author}\nAnnée de publication : {year}\n")
else:
    # Si le site web ne répond pas correctement, on affiche le code d'erreur
    print(f"Erreur : {response.status_code}")