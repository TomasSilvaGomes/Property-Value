import pandas as pd

perth = pd.read_csv('Ficheiros/perth_file.csv')

melbourne = pd.read_csv('Ficheiros/melb_data.csv')
melbourne['date_sold'] = melbourne['date_sold'].str[3:]
melbourne['date_sold'] = melbourne['date_sold'].str.replace(' ', '')

delhi = pd.read_csv('Ficheiros/Delhi_v2.csv')
delhi['price']= delhi['price'] / 83 #Conversão de rúpias para dólares
concat = pd.concat([perth, melbourne])

ficheiro_concat = pd.concat([concat, delhi])
#Eliminar as colunas que não são necessárias para a análise:
ficheiro_concat  = ficheiro_concat.drop(columns=['post_code','address', 'suburb', 'garage', 'floor_area', 'cbd_dist', 'nearest_stn', 'nearest_stn_dist', 'nearest_sch', 'nearest_sch_dist', 'nearest_sch_rank','rooms', 'type', 'method', 'sellerg', 'distance', 'car', 'buildingarea', 'councilarea', 'regionname', 'propertycount','balcony', 'status', 'neworold', 'parking', 'furnished_status', 'lift', 'landmarks', 'type_of_building', 'desc', 'price_sqft'])
ficheiro_concat.to_csv('Ficheiros/ficheiro_concat.csv')