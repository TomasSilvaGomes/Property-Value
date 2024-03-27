import pandas as pd

perth = pd.read_csv('Ficheiros/perth_file.csv')

melbourne = pd.read_csv('Ficheiros/melb_data.csv')
melbourne['date_sold'] = melbourne['date_sold'].str[3:]
melbourne['date_sold'] = melbourne['date_sold'].str.replace(' ', '')

delhi = pd.read_csv('Ficheiros/Delhi_v2.csv')

concat = pd.concat([perth, melbourne])

ficheiro_analise = pd.concat([concat, delhi])
#Eliminar as colunas que não são necessárias para a análise:
ficheiro_analise  = ficheiro_analise.drop(columns=['address', 'suburb', 'garage', 'floor_area', 'cbd_dist', 'nearest_stn', 'nearest_stn_dist', 'nearest_sch', 'nearest_sch_dist', 'nearest_sch_rank','rooms', 'type', 'method', 'sellerg', 'distance', 'car', 'buildingarea', 'councilarea', 'regionname', 'propertycount','balcony', 'status', 'neworold', 'parking', 'furnished_status', 'lift', 'landmarks', 'type_of_building', 'desc', 'price_sqft'])

ficheiro_analise.to_csv('Ficheiros/ficheiro_analise.csv')