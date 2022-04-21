#!/usr/bin/env python3
import pandas as pd
import operator
import sys

def process_data(data_file_name, taxi_zones_file_name):
    #data_file_name = 'yellow_tripdata_2021-01.csv'
    #taxi_zones_file_name = 'taxi_zones.csv'
    df_data = pd.read_csv(data_file_name)
    df_zones = pd.read_csv(taxi_zones_file_name)

    quantile = df_data.trip_distance.quantile(0.95)
    #Comentar que existen ID de zona mayores a 263
    df_filtered_data = df_data[(df_data['DOLocationID'] <= 263) & (df_data['trip_distance'] > quantile)]
    DOLocationID_dict = {}
    count = 0

    for index, row in df_filtered_data.iterrows():
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
    #print("RESULTADOS:")
    #print(df_results)
    return df_results


def print_result(result):
    print(result)


def save_result(result, result_file_name):
    result.to_csv(result_file_name, index=False)



if __name__== "__main__":

    if len(sys.argv) != 4:
        print("Argument number incorrect")
        print("First argument: Input data filname")
        print("Second argument: Taxi zones filename")
        print("Third argument: Result data filename")
        exit(0)
    '''if sys.argv[1] is None:
        print("Unknow filename is missing")
        exit(0)
    elif sys.argv[2] is None:
        print("Unknown result filename")
        exit(0)'''

    #Input parameter
    file_name = str(sys.argv[1])
    taxi_zones_file_name = str(sys.argv[2])
    result_file_name= str(sys.argv[3])
    result = process_data(file_name, taxi_zones_file_name)
    print_result(result)
    save_result(result, result_file_name)