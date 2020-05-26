## Analyse du traffic de taxis à NYC


Ce repo git a été construit pour étudier le comportement des trajets des taxis new yorkais.
On a utilisé les données suivantes (https://www.kaggle.com/c/nyc-taxi-trip-duration/data) pour calculer 4 indicateurs:

- la vitesse moyenne de chaque trajet,
- le nombre de trajets effectués en fonction du jour de la semaine,
- le nombre de trajets effectués en fonction de l’horaire de la journée par tranche de 4h,
- le nombre de km parcourus par jour de la semaine.

### Installation

Pour faire tourner ce code, il faut la version 3.7.3 de Python ainsi que les différents packages indiqués dans le requirements.txt

### Utilisation

Un extrait de la base de données train.csv de kaggle est présent dans le dossier Data. Le path a donc été dirigé vers ce dossier pour pouvoir utiliser l'extrait de données: train_sample.csv

Le processus est le même pour calculer les différents indicateurs:

$ python3 Indicators/nom_de_l'indicateur

Ensuite, des fichiers vont se créer automatiquement dans le dossier data avec les résultats indiqués.

### Tests    

Deux sortes de tests ont été construit dans le dossier Test:

- le fichier "Tests.py" rassemble quelques tests à effectuer sur le jeu de données initial ("train_sample.csv") afin de s'assurer de certaines caractéristiques (nombre de features, types de certaines variables, valeurs nulles et valeur particulières)
- le fichier "Tests_post_indicators.py" qui ne peut être compilé seulement après la construction des différents indicateurs.

Le code pour compiler ces tests fonctionnent de la même manière que celui pour les indicateurs:

$ python3 Test/nom_du_test

Pour réaliser ce travail, nous avons utiliser exclusivement python et les librairies usuelles de traitement de données (pandas, numpy) afin de gagner du temps.
Cependant, après avoir fait des tests de calcul de vitesse sur l'ensemble du dataframe, il semblerait que la méthode choisit prenne du temps et il aurait sans doute été préférable d'utiliser des API Spark.
