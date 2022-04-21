#!/usr/bin/env python3
import pandas as pd
import operator

data_file_name = 'yellow_tripdata_2021-01.csv'
taxi_zones_file_name = 'taxi_zones.csv'
df_data = pd.read_csv(data_file_name)
df_zones = pd.read_csv(taxi_zones_file_name)
#print(df_data.head(5))
#print(df_zones)
#print(df_zones['LocationID'])
#print(df_zones['borough'])
#print(df_zones['zone'])
#print(df.trip_distance.quantile(0.94))
#print(df.trip_distance > df.trip_distance.quantile(0.95))
#print(df['PULocationID'].value_counts().sort_values().tail(10))

quantile = df_data.trip_distance.quantile(0.95)
df_data = df_data[(df_data['DOLocationID'] <= 263) & (df_data['trip_distance'] > quantile)]
DOLocationID_dict = {}
count = 0

for index, row in df_data.iterrows():
    #print(index, row)
    #Check if 'trip_distance' row value is greater that the quantile of 'trip_distance' column value
    #if row.trip_distance > quantile:
    count += 1

    if row.DOLocationID not in DOLocationID_dict:
        DOLocationID_dict[row.DOLocationID] = 1

    elif row.DOLocationID in DOLocationID_dict:
        DOLocationID_dict[row.DOLocationID] = DOLocationID_dict[row.DOLocationID] + 1


print("DOLocationID_dict    {}".format(DOLocationID_dict))
sorted_DOLocationID_dict = sorted(DOLocationID_dict.items(), key=operator.itemgetter(1), reverse=True)
print("sorted_DOLocationID_dict    {}".format(sorted_DOLocationID_dict))


trips_list = list()
borough_list = list()
zone_list = list()

for item in sorted_DOLocationID_dict[:10]:
    print(item)
    if item[0] < 223:
        location_id = item[0]
        trips_number = item[1]
        end_borough = df_zones[df_zones.LocationID == location_id].borough.tolist()
        end_zone = df_zones[df_zones.LocationID == location_id].zone.tolist()

        trips_list.append(trips_number)
        borough_list.append(' '.join(end_borough))
        zone_list.append(' '.join(end_zone))



results = {'Trips': trips_list,
           'end_borough': borough_list,
           'end_zone': zone_list}

df_results = pd.DataFrame(results)
print("RESULTADOS:")
print(df_results)




