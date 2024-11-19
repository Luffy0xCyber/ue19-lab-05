
# Application d'Information sur les Personnes les Plus Recherchées par le FBI
[![Build Status](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c7c_Build-Passing-brightgreen.svg)](https://github.com/Luffy0xCyber/ue19-lab-05/actions)
[![License](https://img.shields.io/badge/License-Unlicensed-blue.svg)](https://github.com/Luffy0xCyber/ue19-lab-05/blob/main/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/Luffy0xCyber/ue19-lab-05)]()
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Luffy0xCyber/ue19-lab-05)]()
[![GitHub watchers](https://img.shields.io/github/watchers/Luffy0xCyber/ue19-lab-05)]()
[![GitHub contributors](https://img.shields.io/github/contributors/Luffy0xCyber/ue19-lab-05)]()
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Luffy0xCyber/ue19-lab-05)]()

## Description du Projet

Cette application Python récupère et affiche des informations sur les personnes les plus recherchées par le FBI. L'application utilise l'API publique du FBI pour obtenir les données et les présente de manière lisible. 

## Table des Matières

1. [Description du Projet](#description-du-projet)
2. [Comment Installer et Exécuter le Projet](#comment-installer-et-exécuter-le-projet)
3. [Comment Utiliser le Projet](#comment-utiliser-le-projet)
4. [Crédits](#crédits)
5. [Licence](#licence)

## Comment Installer et Exécuter le Projet

Pour exécuter ce projet localement, suivez ces étapes :

1. **Cloner le dépôt :**
    ```sh
    git clone https://github.com/Luffy0xCyber/ue19-lab-05.git
    cd ue19-lab-05
    ```

2. **Construire l'image Docker :**
    ```sh
    docker build -t fbi-most-wanted-app .
    ```

3. **Exécuter le conteneur Docker :**
    ```sh
    docker run --rm fbi-most-wanted-app
    ```

## Comment Utiliser le Projet

Une fois l'application en cours d'exécution, elle récupérera et affichera des informations sur les personnes les plus recherchées par le FBI. Les informations incluent :

- Nom Complet
- Sexe
- Race
- Caractéristiques Physiques (Cheveux, Yeux, Taille)
- Récompense (si disponible)
- Description (si disponible)
- Message d'Avertissement (si disponible)

L'application affichera le nombre total de personnes recherchées et les détails des 10 premières personnes.

## Crédits

Ce projet a été développé par [Anas Alias Luffy](https://github.com/Luffy0xCyber).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/anaself/)

## Licence

Ce projet n'est pas sous licence. Libre à vous de l'utiliser, de le modifier et de le distribuer comme bon vous semble.

