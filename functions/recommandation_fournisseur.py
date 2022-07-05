import pandas as pd
import numpy as np


# calcul de la distance 
def calcul_distance(data, villes, ville_acheteur):
    temp = villes[villes.city == ville_acheteur].reset_index(drop=True)
    data['Distance'] = list(zip(data.lat, data.lng))
    data['Distance'] = data['Distance'].apply(lambda x : geopy.distance.geodesic(x, (temp['lat'][0],temp['lng'][0])).km)
    return df


def calcul_score(df, villes, ville_acheteur, produit, nom_ferme):
    
    df = calcul_distance(df, villes, ville_acheteur)
    df['Ville acheteur'] = [ville_acheteur]*200
    
    #définir la ferme et le produit par rapport  auquel on calcule le score
    x_0 = df[df['Nom de la ferme'] == nom_ferme].reset_index(drop=True)
    
    #choisir fermes qui produisent le meme produit uniquement
    sub_df = df[(df['Produit issu de la ferme'] == produit) 
                & (df['Label bio'] == x_0['Label bio'][0])]

    num_columns = ['Surface', 'Emmission transport', 'Emmission type packaging', 'Masse packaging', 'Distance']
    cat_columns = ['Label bas carbone', 'Label bio', 'Label produit fermier', 'Label aop']
    
    delta_num = pd.DataFrame([])
    for c in num_columns:
        #mesurer les deltas en pourcentage pour les colonnes numériques
        delta_num[c] = sub_df[c].apply(lambda x: (x - x_0[c])/x_0[c])

    delta_cat = pd.DataFrame([])
    for c in cat_columns:
        #mesurer les deltas net pour les colonnes catégoriques (0 et 1 des labels)
        delta_cat[c] = sub_df[c].apply(lambda x: (x - x_0[c]))
    
    sub_df['CO2'] = sub_df['Distance'].multiply(sub_df['Emmission transport'])+sub_df['Emmission type packaging'].multiply(sub_df['Masse packaging'])
    
    x_0['CO2'] = x_0['Distance']*x_0['Emmission transport']+x_0['Emmission type packaging']*x_0['Masse packaging']
    
    sub_df['% CO2 reco vs init'] = 1 + sub_df['CO2'].apply(lambda x: (x - x_0['CO2'])/x_0['CO2'])
    sub_df['CO2 norm'] = sub_df['CO2'].apply(lambda x: (x- min(sub_df['CO2']))/(max(sub_df['CO2'])-min(sub_df['CO2'])))                                                                                                                         
    sub_df['score'] = 0.7 - ((sub_df['CO2 norm']) - 0.2 * sub_df['Label bas carbone'] - 0.1 * sub_df['Label aop'])
    
    sub_df = sub_df.sort_values('score', ascending=True)
    
    return sub_df


def calcul_score_sans_ferme(data, villes, ville_acheteur, ingredient):
    temp = data.copy()
    
    #temp['Ville acheteur'] = [ville_acheteur]*200
    
    temp = temp[temp['Produit issu de la ferme'] == ingredient].reset_index(drop=True)
    
    temp['CO2'] = temp['Distance'].multiply(temp['Emmission transport'])+temp['Emmission type packaging'].multiply(temp['Masse packaging'])
    
    temp['CO2 norm'] = temp['CO2'].apply(lambda x: (x- min(temp['CO2']))/(max(temp['CO2'])-min(temp['CO2'])))                                                                                                                         
    temp['score'] = 0.7 - ((temp['CO2 norm']) - 0.2 * temp['Label bas carbone'] - 0.1 * temp['Label aop'])
    
    reco = temp.sort_values('score', ascending = False)
    
    return reco


def recommender_fournisseur(data, villes, ville_acheteur, produit, nom_ferme = None, metric = 'score'):
    
    if nom_ferme is None : 
        df_resultat = calcul_score_sans_ferme(data, villes, ville_acheteur, produit).sort_values(by = metric, ascending = False)
        resultat = df_resultat.head(10)
    else : 
        df_resultat = calcul_score(data, villes, ville_acheteur, produit).sort_values(by = metric, ascending = False)
        resultat = df_resultat.head(10)
    
    return resultat