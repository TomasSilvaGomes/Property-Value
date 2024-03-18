import pandas as pd
import tabulate

import matplotlib.pyplot as plt


perth_file = pd.read_csv('perth_file.csv')

#Drop all variables except price, bedrooms, bathrooms, adress , date_sold, suburb, postcode:
perth = perth_file.drop(columns=['garage','floor_area','build_year','cbd_dist','nearest_stn','nearest_stn_dist','latitude','longitude','nearest_sch','nearest_sch_dist','nearest_sch_rank'])
#criar uma coluna com o nome rooms e atribuir o valor de bedrooms + bathrooms:



melbourne= pd.read_csv('melb_data.csv')
melbourne = melbourne.drop(columns=['rooms','type','method','sellerG','distance','car','buildingArea','yearBuilt','councilArea','lattitude','longtitude','regionname','propertycount'])
#criar uma coluna com o nome rooms e atribuir o valor de bedrooms + bathrooms:


merg1= pd.merge(perth, melbourne, how='outer')





#merge thw two datasets after the drop of the columns:
merged1 = pd.concat([perth, melbourne])

