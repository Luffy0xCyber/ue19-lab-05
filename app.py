import requests

# URL de l'API pour avoir les informations sur les personnes "most wanted" du programme FBI
# cf. documentation du FBI => https://www.fbi.gov/wanted/api
API_URL = 'https://api.fbi.gov/wanted/v1/list'

try:
    # Variable response qui va recevoir un code
    response = requests.get(API_URL)

    # Si le code est 200 alors la requête est réussi
    if response.status_code == 200:
        # Convertir les données en json()
        donnee = response.json()
        # le print en commentaire ci-dessous m'a aidé à comprendre la structure et comment c'est organisé
        # print(donnee)

        # Afficher le nombre total de personnes
        print(f"Nombre total de personnes recherchées : {donnee['total']}\n")

        # Parcourir les 10 premières personnes, vous pouvez changer le nombre de personnes à afficher.
        # Attention que ce nombre ne doit pas excéder le nombre total des personnes recherché (cf. print jsute au-dessus)
        for person in donnee['items'][:10]:
            print("*" * 50)  # Ligne de séparation pour mieux visualiser

            # Informations de base à savoir le nom complet, Sexe et la Race
            print(f"Nom Complet: {person.get('title', 'Non spécifié')}")
            print(f"Sexe: {person.get('sex', 'Non spécifié')}")
            print(f"Race: {person.get('race', 'Non spécifiée')}")

            # C les informations concenrnant les cheveux, Yeux et la taille
            print("\nCaractéristiques physiques:")
            print(f"Cheveux: {person.get('hair', 'Non spécifié')}")
            print(f"Yeux: {person.get('eyes', 'Non spécifié')}")
            # Attention qu'ici la taille est en inches (utilisée aux États-Unis)
            if 'height_min' in person and 'height_max' in person:
                print(f"Taille: {person['height_min']} - {person['height_max']}")

            # Une récompense si c disponible
            if 'reward_text' in person and person['reward_text']:
                print(f"\nRécompense: {person['reward_text']}")

            # Une Description si c disponible
            if 'description' in person and person['description']:
                print("\nDescription:")
                print(person['description'])

            # Avertissement si c disponible
            if 'warning_message' in person and person['warning_message']:
                print("\nAVERTISSEMENT:")
                print(person['warning_message'])

            print("\n")  # Ligne vide pour aider pour la lisibilité
# tous les excepts c'est pour les cas d'erreurs !
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête : {e}")
except KeyError as e:
    print(f"Erreur dans la structure des données : {e}")
except Exception as e:
    print(f"Une erreur inconnue s'est produite : {e}")