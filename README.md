# Géolocalisation d'Adresses IP

## Démo
![DEMOOOOO](https://github.com/AlphaxHotelxMikexEchoxDelta/GeoIP/assets/95902084/ef57c047-9f3d-424c-913b-516717d88a39)


## Table des matières

1. [Compréhension du Projet](#compréhension-du-projet)
2. [Compréhension des Données](#compréhension-des-données)
3. [Captures d'écran des Visualisations/Résultats](#captures-décran-des-visualisationsrésultats)
4. [Technologies Utilisées](#technologies-utilisées)
5. [Installation](#installation)
6. [Utilisation](#utilisation)
7. [Definition](#definition)

## Compréhension du Projet

Ce projet consiste en une application lourde interagissant avec une API REST pour géolocaliser des adresses IP. Une interface graphique permet à l'utilisateur d'entrer une adresse IP, puis l'application interroge une autre API REST (Shodan) pour obtenir des informations de géolocalisation sur cette adresse IP.

## Compréhension des Données

Les données utilisées proviennent de l'API REST Shodan qui fournit des informations de géolocalisation sur les adresses IP.

## Technologies Utilisées

- Python
- PyQt5
- FastAPI
- requests
- Shodan

## Installation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt sur votre machine locale.
3. Installez les dépendances en exécutant la commande suivante dans votre terminal :

```bash
pip install fastapi pyqt5 requests shodan
```

## Utilisation

Voici comment vous pouvez ajouter les instructions pour lancer le serveur et accéder à l'API à votre README :

### Lancement du Serveur

Pour lancer le serveur, exécutez la commande suivante dans votre terminal, en vous assurant d'être dans le répertoire où se trouve le fichier `webser.py` :

```bash
uvicorn webser:app --reload
```

Cette commande démarre le serveur uvicorn et charge l'application FastAPI définie dans le fichier `webser.py`.

### Accès à l'API

Une fois le serveur démarré, ouvrez un navigateur web et accédez à l'URL suivante :

[http://127.0.0.1:8000](http://127.0.0.1:8000)

Cela affichera la documentation interactive de l'API FastAPI, qui répertorie toutes les routes disponibles ainsi que leurs paramètres et schémas de réponse. Vous pouvez également tester les différentes routes directement à partir de cette documentation.

---

N'oubliez pas d'ajuster le chemin de la commande `uvicorn` en fonction de l'emplacement réel de votre fichier `webser.py`.


1. Lancez le serveur en exécutant le script `webser.py`.
2. Lancez l'application cliente en exécutant le script `client.py`.
3. Dans l'interface graphique qui apparaît, entrez l'adresse IP que vous souhaitez géolocaliser, puis cliquez sur le bouton "Send".
4. Les informations de géolocalisation seront affichées dans l'interface graphique.


# Definition

Une **[API REST](https://www.redhat.com/fr/topics/api/what-is-a-rest-api)** (également appelée API RESTful) est une interface de programmation d'application (API ou API web) qui respecte les contraintes du style d'architecture REST et permet d'interagir avec les services web RESTful. L'architecture REST (Representational State Transfer) a été créée par l'informaticien Roy Fielding.

Une API est un ensemble de définitions et de protocoles qui facilite la création et l'intégration de logiciels d'applications. Elle est parfois considérée comme un contrat entre un fournisseur d'informations et un utilisateur d'informations, qui permet de définir le contenu demandé au consommateur (l'appel) et le contenu demandé au producteur (la réponse).

Une API RESTful doit remplir plusieurs critères, notamment :

- Une architecture client-serveur constituée de clients, de serveurs et de ressources, avec des requêtes gérées via HTTP
- Des communications client-serveur stateless, c'est-à-dire que les informations du client ne sont jamais stockées entre les requêtes GET, qui doivent être traitées séparément, de manière totalement indépendante
- La possibilité de mettre en cache des données afin de rationaliser les interactions client-serveur
- Une interface uniforme entre les composants qui permet un transfert standardisé des informations

**[FastAPI](https://fastapi.tiangolo.com/fr/features/)**, quant à lui, est un framework web moderne pour construire des APIs avec Python 3. Il est basé sur des standards ouverts comme OpenAPI pour la création d'API et fournit une documentation automatique, une validation des données, la sécurité et l'authentification intégrées, ainsi que d'autres fonctionnalités avancées pour faciliter le développement d'API robustes et performantes.
