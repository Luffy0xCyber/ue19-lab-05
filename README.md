# Application de Recherche de Livres sur la Cybersécurité
[![Build Status](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c7c_Build-Passing-brightgreen.svg)](https://github.com/Luffy0xCyber/ue19-lab-05/actions)
[![License](https://img.shields.io/badge/License-Unlicensed-blue.svg)](https://github.com/Luffy0xCyber/ue19-lab-05/blob/main/LICENSE)

## Description du Projet

Cette application Python récupère et affiche des informations sur les livres liés à la cybersécurité. L'application utilise l'API publique d'Open Library pour obtenir les données et les présente de manière lisible.

## Table des Matières

1. [Description du Projet](#description-du-projet)
2. [Comment Installer et Exécuter le Projet](#comment-installer-et-exécuter-le-projet)
3. [Comment Utiliser le Projet](#comment-utiliser-le-projet)
4. [Déploiement sur Digital Ocean](#déploiement-sur-digital-ocean)
5. [Crédits](#crédits)
6. [Licence](#licence)

## Comment Installer et Exécuter le Projet

Pour exécuter ce projet localement, suivez ces étapes :

1. **Cloner le dépôt :**
    ```sh
    git clone https://github.com/Luffy0xCyber/ue19-lab-05.git
    cd ue19-lab-05
    ```

2. **Construire l'image Docker :**
    ```sh
    docker build -t cybersecurity-books-app .
    ```

3. **Exécuter le conteneur Docker :**
    ```sh
    docker run --rm cybersecurity-books-app
    ```

## Comment Utiliser le Projet

Une fois l'application en cours d'exécution, elle récupérera et affichera des informations sur les livres liés à la cybersécurité. Les informations incluent :

- Titre
- Auteur(s)
- Année de publication
- Éditeur(s)
- Sujets

L'application affichera les détails des 10 premiers livres trouvés.

## Déploiement sur Digital Ocean

Ce projet a été testé sur un droplet Digital Ocean et a fonctionné en utilisant les commandes Docker mentionnées ci-dessus.

## Crédits

Ce projet a été développé par [Anas Alias Luffy](https://github.com/Luffy0xCyber).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/anaself/)

## Licence

Ce projet n'est pas sous licence. Libre à vous de l'utiliser, de le modifier et de le distribuer comme bon vous semble.