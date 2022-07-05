import pandas as pd
import numpy as np
from ast import literal_eval
from gensim.models import keyedvectors

data_carbone_total_loaded = pd.read_csv('data/data_carbon_total_full_base_carb.csv')
saved_model = keyedvectors.KeyedVectors.load('model1.kvmodel')


def isNaN(string):
    return string != string


def reco(ingredient='fraise'):  
    # Information on the original product
    info_origin = pd.DataFrame(data_carbone_total_loaded[data_carbone_total_loaded.ingredients==ingredient]) \
        .reset_index(drop=True)
    emission_origin = info_origin.empreinte_carbone[0]
    try:
        categorie_origin = literal_eval(info_origin.categorie[0])
    
    except:
        categorie_origin = np.nan
        
    # Find similarities
    top_sim = pd.DataFrame(saved_model.most_similar(ingredient, topn=20), columns=['ingredient', 'similarity'])
    
    # We keep the reco within 40% similarity coeff of the best reco
    top_sim = top_sim[top_sim.similarity>(max(top_sim.similarity)-max(top_sim.similarity)*0.4)]
    
    # Add carbon emissions
    carbon_emission = []
    categorie = []
    for sim_ind in range(top_sim.shape[0]):
        ing = top_sim.ingredient[sim_ind]
        carbon_emission += list(data_carbone_total_loaded[data_carbone_total_loaded.ingredients==ing].empreinte_carbone.values)
        categorie += list(data_carbone_total_loaded[data_carbone_total_loaded.ingredients==ing].categorie.values)
    top_sim['carbon_emission'] = carbon_emission
    top_sim['categorie'] = categorie

    # We keep reco with less emission that the original product
    top_sim = top_sim[top_sim.carbon_emission<emission_origin]
    
    # Info on the original ingredient to add
    to_add_origin = pd.DataFrame({"ingredient":[ingredient], 
                                  "similarity": [1], 
                                  "carbon_emission":[emission_origin],
                                  "categorie":[categorie_origin]})

    try:
        # Reco with a categorie
        with_cat = top_sim[top_sim.categorie.notna()]
        
        # Reco with the same categorie
        with_same_cat = with_cat[np.array(with_cat.categorie.apply(lambda x: np.sum(np.array([c in x for c in categorie_origin]))))>1]
        with_same_cat = with_same_cat.sort_values('carbon_emission')

        # Rest
        rest = top_sim.drop(with_same_cat.index)
        rest = rest.sort_values('carbon_emission')
        
        # Add info on the original ingredient
        final_reco = pd.concat([with_same_cat, rest, to_add_origin], axis=0)
        
    except:
        # If no categorie
        final_reco = top_sim.sort_values('carbon_emission')
        final_reco = pd.concat([final_reco, to_add_origin], axis=0)
        
    return final_reco