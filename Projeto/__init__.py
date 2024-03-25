import pandas as pd

perth_file = pd.read_csv('perth_file.csv')

perth = perth_file.drop(columns=['address', 'suburb', 'garage', 'floor_area', 'cbd_dist', 'nearest_stn', 'nearest_stn_dist', 'nearest_sch', 'nearest_sch_dist', 'nearest_sch_rank'])

melbourne = pd.read_csv('melb_data.csv')
melbourne = melbourne.drop(columns=['address', 'suburb', 'rooms', 'type', 'method', 'sellerg', 'distance', 'car', 'buildingarea', 'councilarea', 'regionname', 'propertycount'])
#eliminate the first 2 caracters of the column 'date_sold':
melbourne['date_sold'] = melbourne['date_sold'].str[3:]
melbourne['date_sold'] = melbourne['date_sold'].str.replace(' ', '')


delhi = pd.read_csv('Delhi_v2.csv')
delhi = delhi.drop(columns=['address', 'balcony', 'status', 'neworold', 'parking', 'furnished_status', 'lift', 'landmarks', 'type_of_building', 'desc', 'price_sqft'])

concat = pd.concat([perth, melbourne])
ficheiro_analise = pd.concat([concat, delhi])
ficheiro_analise.to_csv('ficheiro_analise.csv', index=False)