# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:18:26 2021

@author: kaoua
"""

import pandas as pd
import numpy as np


def get_monthyear(chaine, num, sep='-'):
    liste = str(chaine).split(sep)
    return liste[num]
def get_day(chaine, num, sep=' '):
    liste = str(chaine).split(sep)
    return liste[num]
def get_hourminute(chaine, num, sep=':'):
    liste = str(chaine).split(sep)
    return liste[num]

def Data_processing(df):
    #print("Taille du ficher = ", df.shape)
    ############################################
    # Conversion des timestamps en format date #
    ############################################
    #print('\t Conversion des timestamps en format date')
    date_l = []
    for i in df['launched_at']:
        if i != '':
            date_l.append(pd.Timestamp(i, unit='s'))
            
    df['lancement'] = date_l
    
    date_l = []
    for i in df['deadline']:
        if i != '':
            date_l.append(pd.Timestamp(i, unit='s'))
    df['date_limite'] = date_l
    
    
    
    df['duree_projet'] = df['date_limite'] - df['lancement']
    
    df['duree_projet'] = df['duree_projet'].apply(get_day, args=[0])
   
    
    ####################################################################
    # Construction des variables : Année, mois, jour, heure  et minute #
    ####################################################################
    
    j = df['lancement'].apply(get_monthyear, args=[2])
    j = j.apply(get_day, args=[0])
    m = df['lancement'].apply(get_monthyear, args=[1])
    a = df['lancement'].apply(get_monthyear, args=[0])
    
    h = df['lancement'].apply(get_monthyear, args=[2])
    h = h.apply(get_day, args=[1])
    hh = h.apply(get_hourminute, args=[0])
    mm = h.apply(get_hourminute, args=[1])
    
     
    
    
    df['annee'] = a
    df['mois'] = m
    df['jour'] = j
    df['heure'] = hh
    df['minute'] = mm
    
    ###########################################################
    # Suppression des variables inutiles avec beaucoup de NaN #
    ###########################################################
    
    df = df.drop(['friends', 'is_backing', 'is_starred', 'permissions'], axis=1)
    
    ############################################################################################
    # Création des variables : cat_id, cat_name et cat_prim à partir de la variable 'category' #
    ############################################################################################
    
    cat_id = []
    cat_name = []
    cat_prim = []
    
    for i in df['category']:    
        s = i.replace("{" ,"")
        s = s.replace("}" ,"")
        dico = {}
        liste = s.split(',')
        #print(liste)
        for i in liste:
            o = i.split(':')
            m = o[0].strip('"')
            n = o[1].strip('"')
            dico[m] =n
        if 'parent_name' not in dico:
            dico['parent_name'] = 'None'
        
        cat_id.append(int(dico['id']))
        cat_name.append(dico['name'])
        cat_prim.append(dico['parent_name'])
    
    df['cat_id'] = cat_id
    df['cat_name'] = cat_name
    df['cat_prim'] = cat_prim
    
    #################################################
    # Création des variables : crea_name et crea_id #
    #################################################
    
    crea_id = []
    crea_name = []
    
    
    for i in df['creator']:    
        s = i.replace("{" ,"")
        s = s.replace("}" ,"")
        dico = {}
        liste = s.split(',')
        #print(liste)
        for p in liste:
            o = p.split(':')
            #print(o)
            if o[0] == '"id"' or o[0] == '"name"':
                m = o[0].strip('"')
                n = o[1].strip('"')
                dico[m] =n
        
        
        crea_id.append(int(dico['id']))
        crea_name.append(dico['name'])
        
    
    df['crea_id'] = crea_id
    df['crea_name'] = crea_name    
    
    
    ##################################### 
    # Création de la variable : proj_id #
    #####################################
    
    proj_id = []
    for i in df['profile']:    
        s = i.replace("{" ,"")
        s = s.replace("}" ,"")
        dico = {}
        liste = s.split(',')
        #print(liste)
        for p in liste:
            o = p.split(':')
            #print(o)
            if o[0] == '"id"':
                m = o[0].strip('"')
                n = o[1].strip('"')
                dico[m] =n
        
        
        proj_id.append(int(dico['id']))
        #crea_name.append(dico['name'])
        
    
    df['proj_id'] = proj_id
    
    
    #########################################
    # Création de la variable url du projet #
    #########################################
    
    url=[]
    for i in df['urls']:    
            s = i.replace("{" ,"")
            s = s.replace("}" ,"")
          
            liste = s.split('"')
            url.append(liste[5])
    df['url'] = url
    
    
    #############################################
    # Création de la variable cible : `success` #
    #############################################
    
    statut = []
    for objectif, resultat in zip(df['goal'], df['pledged']):
        if resultat >= objectif:
            statut.append(1)
        else:
            statut.append(0)
        
    df['success']= statut
    
    ########################################### 
    # Création de la variable : proj_desc_len #
    ###########################################
    
    longueur=[]
    
    for desc in df['blurb']:
        if not isinstance(desc, str):
            longueur.append(0)
        else:
            #print(desc)
            longueur.append(len(desc))
    
    df['proj_desc_len']=longueur
    
    ###########################################
    # Création de la variable : coup_de_coeur # 
    ###########################################
    
    
    
    ###############################
    # Réorganisation des colonnes #
    ###############################
    
    
    data = pd.DataFrame()
    # variables temporelles
    data['lancement'] = df['lancement']
    data['annee'] = df['annee']
    data['mois'] = df['mois']
    data['jour'] = df['jour']
    data['heure'] = df['heure']
    data['jour_semaine'] = df['lancement'].dt.weekday
    # variables du projet
    data['proj_id'] = df['proj_id']
    data['proj_name'] = df['name']
    data['proj_desc_len'] = df['proj_desc_len']
    data['country'] = df['country_displayable_name']
    data['goal'] = df['goal'] * df['fx_rate']
    data['nbr']= np.ones(len(data['goal']))
    
    
    data['date_limite'] = df['date_limite']
    data['duree_projet'] = df['duree_projet']
    data['url']=df['url']
    data['spot_light'] = df['spotlight']
    data['nbr_backers'] = df['backers_count']
    data['pledged'] = df['usd_pledged']
    #data['coup_de_coeur'] = coeur
    
    # Catégorie du projet
    data['cat_id'] = df['cat_id']
    data['cat_prim']= df['cat_prim']
    data['cat_name']= df['cat_name']
    
    
    
    
    # variables sur le créateur du projet
    data['crea_id'] = df['crea_id']
    data['crea_name'] = df['crea_name']
    
    # variable cible
    data['success']= df['success']
    
    
    return data