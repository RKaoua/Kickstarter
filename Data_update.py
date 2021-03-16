# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:17:24 2021

@author: kaoua
"""
import pandas as pd
import numpy as np
from Data_processing import Data_processing

def Data_update():
    
    ##############################
    # Importation du 1er fichier #
    ##############################
    print('Initialisation du fichier de base')
    
    data = pd.read_csv("kickstarter_files/Kickstarter.csv")
    data = Data_processing(data)
    
    ####################################################
    # Importation des autres fichiers et concaténation #
    ####################################################
    
    for i in range(1,58,1):
        if i <10:
            num = '00'+str(i)
        else:
            num= '0'+str(i)
        print('Importation et traitement du fichier', num+'/057')    
        nom_fichier = 'kickstarter_files/Kickstarter'+num+'.csv'
        df = pd.read_csv(nom_fichier)
        df = Data_processing(df)
        data = pd.concat([data, df])
        nom_fichier = 'dataset_kickstarter_brut.csv'
        data.to_csv(nom_fichier, index=True)
    
    data = data.sort_values(by='lancement', ascending=True)
    indexe = np.arange(0,data.shape[0])
    data['indexe'] = indexe
    
    data = data.set_index('indexe')
    
    
    ##########################################################
    # Correction des catégories primaires classées en 'None' #
    ##########################################################
    print('\n Finalisation et regroupement en un seul fichier')
    #reste = data[data['cat_prim']=='None']['cat_id'].unique()
    
    for indexe, cat, cat_id in zip(data['cat_prim'].index, data['cat_prim'],data['cat_id']):
        if cat == 'None':
            
            vrai_cat = data[data['cat_id']==cat_id]['cat_name'].value_counts().index.values[0]
            #print(indexe,',',cat,',',',', cat_id,',', vrai_cat)
            data.loc[indexe, 'cat_prim'] = vrai_cat
            data.loc[indexe, 'cat_name'] = 'others'
    
    # for cat_id in reste:
    #     indexes = data[data['cat_id']==cat_id]['cat_prim'].index.values
    #     vrai_cat = data[data['cat_id']==cat_id]['cat_name'].value_counts().index.values[0]    
    #     for ind in indexes:
    #         data.loc[ind, 'cat_prim'] = vrai_cat
    #         data.loc[ind, 'cat_name'] = 'others'
    
    
    #rest = data[data['cat_prim']=='None']['cat_id']
    
    ##################################################################
    # Suppression des projets dupliqués et enregistrement du Dataset #
    ##################################################################
   
    data = data.drop_duplicates(subset='proj_id', keep='first', inplace=False)
    nom_fichier = 'dataset_kickstarter.csv'
    data.to_csv(nom_fichier, index=True)
    
    print("Fichier enregistré sous le nom : '"+nom_fichier+"'")
    
    return