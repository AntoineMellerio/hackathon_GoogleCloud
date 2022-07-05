![baniere](https://user-images.githubusercontent.com/74012095/177355542-0d9f9e33-04ca-4684-b107-3de62fba269f.png)
# Hackathon GoogleCloud for climate - Datact
:earth_africa:   Agri-business is responsible of 30% of the world carbon emissions.  
  
:bulb:   Along with 8 other students, we created an SAAS B2B platform to assist product designers and purchasing managers in the eco-conception and eco-supply of agri-food products. You can find in this repository the notebooks that conducted the analysis, as well as the final functions and the final presentation.   

## Plateform description
The plateform is composed of three modules :  
  
  :ear_of_rice: an ingredient recommendation system that takes into account the carbon emissions, the seasonality and the similarity with the initial ingredient. The similarity was obtained by cleaning 80 000 recipes and applying on then the Google NLP model word2vec.  
  
  :tractor: a supplier recommendation system that optimises the supplier's carbon emissions based on the distance to the factory, the transport carbon emissions mean, the supplier's low carbon labels, the supplier's POA label (protected origin appellation), and the carbon impact of packaging used for transport.  
  
  :recycle: a packaging recommendation system based on the packaging material's carbon emission, if it is recycled and its recyclable rate (% of material that will be recycled in the future).  
    
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
  
## Insight of the final tool
### Page 1 : ingredient and packaging recommendation system
![final_tool_1](https://user-images.githubusercontent.com/74012095/177353928-680f72ec-2c09-4ea9-a998-2bcf6033f83e.jpg)
  
### Page 2 : supplier recommendation system   
![final_tool_2](https://user-images.githubusercontent.com/74012095/177355713-d2edabe0-547c-4e9c-88eb-5f98792a52a7.jpg)
