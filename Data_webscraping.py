# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:27:58 2021

@author: kaoua
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup



def Data_webscraping(df):
    import progressbar
    #print('\t WebScapping de la variable : coup_de_coeur')

    phrase_magique = 'Project We Love'
    i = 0
    coeur=[]
    with progressbar.ProgressBar(max_value=len(df['url'])) as bar:
        for lien in df['url']:
            #print('--------------------------')
            if lien[0:11] == 'https://api':
                #print('ligne',i,'lien interdit')
                coeur.append(0)
                i+=1
                continue
            
            page_SC = urlopen(lien)
            soup = BeautifulSoup(page_SC, 'html.parser')
            
            balise1 = soup.select(".type-12.keyboard-focusable:nth-child(1)")
            balise2 = soup.select(".type-12.items-center")
            coup_de_coeur=[]
            for element in balise1:
                coup_de_coeur.append(element.text)
            #print('Balise 1 = ', coup_de_coeur)
            if coup_de_coeur == [] or phrase_magique not in coup_de_coeur:
                for element in balise2:
                    s = element.text
                    s = s.replace("\n" ,"")
                    coup_de_coeur.append(s)
                #print('Balise 2 = ', coup_de_coeur)
            
            if phrase_magique in coup_de_coeur:
                #print('ligne', i, 'Projet coup de coeur')
                coeur.append(1)
            else:
                #print('ligne',i, 'Projet simple')
                coeur.append(0)
            #print('\t ', coup_de_coeur)
            
            i+=1
            bar.update(i)
           
    df['coup_de_coeur'] = coeur
    
    
    
    return df