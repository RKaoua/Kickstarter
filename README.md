# Kickstarter 

Le projet consiste en la mise en place d'un système de classification des projets qui ont réussi/échoué sur la plateforme participatif [KickStarter](https://www.kickstarter.com/), et prédire le succès d’une campagne de financement participatif afin de : 

- Guider les créateurs à réussir la mise en place de leur compagne de projet
- Guider les créateurs dans la prise de décision sur le lancement d'une compagne sur KickStarter en fonction du sujet de leur projet 


## Source des données

Les données proviennent du site [WebRobots](https://webrobots.io/kickstarter-datasets/), elles représentent les projets lancés sur la plateforme Kickstarter depuis Avril 2009, et crawlés par un robot tous les mois depuis mars 2016.

## Ressources utilisés
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
   - Data_processing()
   - Data_webscraping

### Fichiers `csv`

- coup_de_coeur.csv : résultat du webscraping .
- Les fichiers csv stockés dans le dossier `kickstarter_files` représente les dataset bruts tel que téléchargés depuis le site [WebRobots](https://webrobots.io/kickstarter-datasets/) et dézippés

## Modèles réalisés et scores

### Modèles de Régression

- ***Logistic Regression*** :
   - Score : 0.561
   - Matrice de confusion :
   
      Classe prédite |0 | 1
      :--- | --- | ---
      **Classe Réelle**  |  |
      **0** | 0 | 16201 
      **1** | 0 | 20720 

- ***SVM*** :
   - Score : 0.556
   - Matrice de confusion : 
   
      Classe prédite |0 | 1
      :--- | --- | ---
      **Classe Réelle**  |  |
      **0** | 0 | 16201 
      **1** | 0 | 20720 

- ***Decision Tree*** : 
   - Score : 0.760
   - Matrice de confusion : 

      Classe prédite |0 | 1
      :--- | --- | ---
      **Classe Réelle**  |  |
      **0** | 11010 | 5191 
      **1** | 3649 | 17071
   - Feature importance : 
   
      Featrure |	Importance
      :--- | ---
      **cat_id**	| 0.434370
      **coup_de_coeur**	| 0.180460
      **goal**	| 0.140758
      **sous_cat_Playing Cards**	| 0.070796
      **annee**	| 0.033572
      **sous_cat_Hip-Hop**	| 0.028076
      **cat_Art**	| 0.027892
      **sous_cat_Software**	| 0.025456
      **sous_cat_Gadgets**	| 0.019900
      **duree_projet**	| 0.011614
      
 - **Random Forest** : 
   - Score : 0.826
   - Matrice de confusion :
   
      Classe prédite |0 | 1
      :--- | --- | ---
      **Classe Réelle**  |  |
      **0** | 13669 | 2532 
      **1** | 3890 | 16830 

   - Feature importance :

      Feature |	Importance
      :--- | ---
      **goal**	| 0.125031
      **cat_id**	| 0.121634
      **crea_id**	| 0.087198
      **annee**	| 0.083590
      **proj_name_len**	| 0.081325
      **proj_desc_len**	| 0.077024
      **duree_projet**	| 0.073205
      **coup_de_coeur**	| 0.062149
      **sous_cat_others**	| 0.011961
      **sous_cat_Playing Cards**	| 0.010437

Meilleur score de regression obtenu : **0.826** avec un modèle `Random Forest`

### Analyse de sentiments

Pour la partie analyse de sentiments, malheureusement nous ne disposons pas de ressources matériels suffisantes pour faire tourner les algorithmes d'encodages des données `CountVectorizer` , `LabelEncoder` et `OneHotEncoder` sur notre dataset.



