![baniere](https://user-images.githubusercontent.com/74012095/177355542-0d9f9e33-04ca-4684-b107-3de62fba269f.png)
# Hackathon GoogleCloud for climate - Datact
:earth_africa:   Agri-business is responsible of 30% of the world carbon emissions.  
  
:bulb:   Along with 8 other students, we created an SAAS B2B platform to assist product designers and purchasing managers in the eco-conception and eco-supply of agri-food products. You can find in this repository the notebooks that conducted the analysis, as well as the final functions and the final presentation.   

### Table of Contents  
- [Plateform description](#plateform-description)  
- [Outputs of the project](#outputs-of-the-project)  
- [Datasets](#datasets)  
- [Recommendation systems' details](#recommendation-systems-details)
- [Insight of the final tool](#insight-of-the-final-tool)  
***
  
## Plateform description
The plateform is composed of three modules :  
  
  :ear_of_rice: an ingredient recommendation system that takes into account the carbon emissions, the seasonality and the similarity with the initial ingredient.   
  
  :recycle: a packaging recommendation system based on the packaging material's carbon emission, if it is recycled and its recyclable rate (% of material that will be recycled in the future).  
  
  :tractor: a supplier recommendation system that optimises the supplier's carbon emissions based on the distance to the factory, the transport carbon emissions mean, the supplier's low carbon labels, the supplier's POA label (protected origin appellation), and the carbon impact of packaging used for transport.  
  
## Outputs of the project
    
:pick:   The tool was built on Datastudio and is available here :  
https://datastudio.google.com/reporting/37b9ff78-ddf0-48a0-9c39-5edfd342b7c8  
A .pdf version of it is also in this repository. 
  
:white_check_mark:  The final presentation was held in front of 6 people having sustainability positions of responsability in different sectors (Google Cloud, Renault, Thales, INRIA, PRAIRIES).  
  
:trophy:   For this project, our team was awarded with the 1st prize.    
  
## Datasets 
We used 3 open-source datasets :  
- ADEME, Base carbone : carbon emissions of ingredients and coumposed products caused by production
- Agribalyze : carbon emissions of ingredients and coumposed products caused by production
- Open Food Facts : compositions of agri-food products
  
## Recommendation systems' details
### Ingredients 
  1 - This module first relies on a **similarity algorithm**. It was obtained by cleaning 80 000 recipes collected from Open Food Fact and applying the Google NLP model word2vec on them. The model identifies the relationships and roles of the ingredients within the recipes. This allows us to output the top 20 most similar items of any ingredient present in the recipes.  
  
  2 - The second criteria of the module is the **category** of the ingredients, gathered from Agribalyze's dataset. Indeed, the final tool would first recommend ingredients of the same category as the inital one.  
  
  3 - The next step is the **carbon emissions**, collected both from Agribalyze and from the Base Carbone dataset of ADEME.  
  
  4 - Finally, we integrate a **seasonality** dataset built ourselves. It allows us to recommend first ingredients of the season the manufacturer wants to produce at. 
  
## Insight of the final tool
- Page 1 : ingredient and packaging recommendation systems
- Page 2 : supplier recommendation system   
<p align="center">
  <a href="url">
    <img src="https://user-images.githubusercontent.com/74012095/177353928-680f72ec-2c09-4ea9-a998-2bcf6033f83e.jpg" height="560" width="500" >
  <a href="url">
    <img src="https://user-images.githubusercontent.com/74012095/177355713-d2edabe0-547c-4e9c-88eb-5f98792a52a7.jpg" height="650" width="490" >
</p>
