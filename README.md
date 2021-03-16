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
### Notebook Jupyter

- **01_Analyse_exploratoire.ipynb** - Etape 1 : Analyse exploratoire des données
- **02_Processing.ipynb** : Etape 2 - Processing des données
- **03_WebScraping.ipynb** : Etape 3 - Enrichissement du projet avec du WebScraping
- **04_Analyse_statistique_Data_Viz.ipynb** : Etape 4 - Analyse statistique et Data Visualisation 
- **05_Machine_learning.ipynb** : Etape 5 - Machine Learning

### Fichiers Python

- **kickstarter.py** : Contient les fonctions suivantes : 
   - Data_update() 

