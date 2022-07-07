![baniere](https://user-images.githubusercontent.com/74012095/177355542-0d9f9e33-04ca-4684-b107-3de62fba269f.png)
# Hackathon GoogleCloud for climate - Datact
:earth_africa:   Agri-business is responsible for 30% of the world's carbon emissions.  
  
:bulb:   Along with 8 other students, we created an SAAS B2B platform to assist product designers and purchasing managers in the eco-conception and eco-supply of agri-food products. You can find in this repository the notebooks that conducted the analysis, as well as the final functions and the final presentation.   

### Table of Contents  
- [Platform description](#platform-description)  
- [Outputs of the project](#outputs-of-the-project)  
- [Datasets](#datasets)  
- [Recommendation systems' criterias](#recommendation-systems-criterias)
- [Insight of the final tool](#insight-of-the-final-tool)  
***
  
## Platform description
The platform is composed of three modules :  
  
  :ear_of_rice: an ingredient recommendation system that takes into account the carbon emissions, the seasonality and the similarity with the initial ingredient.   
  
  :recycle: a packaging recommendation system based on the packaging material's carbon emission, if it is recycled and its recyclable rate (% of material that will be recycled in the future).  
  
  :tractor: a supplier recommendation system that optimises the supplier's carbon emissions based on the distance to the factory, the transport carbon emissions average, the supplier's low carbon, PDO (Protected Designation of Origin) and bio labels, and the carbon impact of packaging used for transport.  
  
## Outputs of the project
    
:pick:   The tool was built on DataStudio and is available here :  
https://datastudio.google.com/reporting/37b9ff78-ddf0-48a0-9c39-5edfd342b7c8  
A .pdf version of it is also in this repository. 
  
:white_check_mark:  The final presentation was held in front of 6 people having sustainability positions of responsibility in different sectors (Google Cloud, Renault, Thales, INRIA, PRAIRIES).  
  
:trophy:   For this project, our team was awarded with the 1st prize.    
  
## Datasets 
We used 3 open-source datasets :  
- ADEME, Base carbone : carbon emissions of ingredients and composed products caused by production
- Agribalyze : carbon emissions of ingredients and composed products caused by production
- Open Food Facts : compositions of agri-food products  
  
Then, we use information given by the suppliers and distributors on :
- production location
- means of transportation
- packaging
  
## Recommendation systems' criterias
### 1 - Ingredients 
- This module first relies on a **similarity algorithm**.  
The similarity is obtained by cleaning 80 000 recipes collected from Open Food Fact and applying the Google NLP model word2vec on them. The model identifies the relationships and roles of the ingredients within the recipes.  
This allows us to output the top 20 most similar items of any ingredient present in the recipes.  
  
- The second criteria of the module is the **category** of the ingredients, gathered from Agribalyze's dataset. Indeed, the final tool would first recommend ingredients of the same category as the initial one.  
  
- The next step is the **carbon emissions**, collected both from Agribalyze and from the Base Carbone dataset of ADEME. We only output ingredients with less carbon emissions than the initial one.  
  
- Finally, we integrate a **seasonality** dataset built ourselves. It allows us to recommend only the ingredients of the season the manufacturer wants to produce at.  

### 2 - Packaging 
- The first criteria of our packaging recommendation system is its **carbon impact**, taken from the ADEME base carbon dataset.
- The second criteria is the **recyclability** of the matter : is the packaging recycled and what proportion will be recycled in the future ? 
- Finally, we apply a filter on the **type of product** concerned, whether the packaging is a bottle or a label. 

### 3 - Supplier
- The first criteria taken into account by this module is the **carbon impact of transportation**.  
We use pieces of information that will be directly given by the supplier : its location and the means of transportation used. Combined with the location of the platform user's manufacture and with the carbon emissions of every transportation means given by the ADEME Carbone Base dataset, we are able to evaluate the carbon impact of transportation.  
The formula applied is the following:  
$$footprint_{transportation} = footprint_{transportation/km,kg}*distance(location_{Supplier}, location_{Manufacture})*weight_{vehicule}$$

- The second criteria is the **carbon impact of the packaging** of its products. We use the carbon footprint data of the ADEME Base Carbone dataset and the information of the weights of packagings given by the supplier:  
$$footprint_{packaging} = footprint_{packaging/kg}*weight_{packaging}$$

- Finally, the recommendation system gives importance to the **labels** owned by the supplier : low carbon, bio and PDO (Protected Designation of Origin).   
  
## Insight of the final tool

- Page 1 : ingredient and packaging recommendation systems
- Page 2 : supplier recommendation system   

<p align="center">
  <a href="url">
    <img src="https://user-images.githubusercontent.com/74012095/177353928-680f72ec-2c09-4ea9-a998-2bcf6033f83e.jpg" height="560" width="500" >
  <a href="url">
    <img src="https://user-images.githubusercontent.com/74012095/177355713-d2edabe0-547c-4e9c-88eb-5f98792a52a7.jpg" height="650" width="490" >
</p>
