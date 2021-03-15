# Kickstarter 

Le projet consiste en la mise en place d'un système de classification des projets qui ont réussi/échoué sur la plateforme participatif [KickStarter](https://www.kickstarter.com/), et prédire le succès d’une campagne de financement participatif afin de : 

- Guider les créateurs à réussir la mise en place de leur compagne de projet
- Guider les créateurs dans la prise de décision sur le lancement d'une compagne sur KickStarter en fonction du sujet de leur projet 


## Source des données

Les données proviennent du site [WebRobots](https://webrobots.io/kickstarter-datasets/), elles représentent les projets lancés sur la plateforme Kickstarter depuis Avril 2009, et crawlés par un robot tous les mois depuis mars 2016.

## Code et ressources utilisés
- **Python Version** : 3.8.5
- **Librairies**: 
   - pandas, 
   - numpy, 
   - sklearn, 
   - matplotlib, 
   - seaborn, 
   - time,
   - urllib,
   - bs4 : BeautifulSoup
 



## Fichiers du projet

- **Data_update.py** : Effectue la mise à jour du dataset :
- **Data_processing.py** : Effectue le data processing des données comme ceci:
 
    - Conversion des timestamps en format `date`
    - Construction des variables : `Année`, `mois`, `jour`, `heure`  et `minute`
    - Suppression des variables inutiles avec beaucoup de NaN 
    - Création des variables : `cat_id`, `cat_name` et `cat_prim` à partir de la variable *'category'*
    - Création des variables : `crea_name` et `crea_id`
    - Création de la variable : `proj_id`
    - Création de la variable : `url` 
    - Création de la variable cible : `success`
    - Création de la variable : `proj_desc_len`
    - Réorganisation des colonnes
    
- **Data_webscraping.py** : permet de récupérer l'information *"coup de coeur de l'équipe"* de chaque projet et l'enregistre dans la variable `coup_de_coeur` 
 
- **Data_category.py** : effectue un `groupby` du dataset par la variable `cat_prim`
 
- **Data_pays.py** : effectue un `groupby` du dataset par la variable `pays`

