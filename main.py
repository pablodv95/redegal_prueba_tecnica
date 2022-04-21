#!/usr/bin/env python3
import pandas as pd
import operator
import sys

def process_data(data_file_name, taxi_zones_file_name):
    # Variable definition
    DOLocationID_dict = {}
    trips_list = list()
    borough_list = list()
    zone_list = list()

    # Get input data (trip data and taxi zone data)
    df_trips_data = pd.read_csv(data_file_name)
    df_taxi_zones = pd.read_csv(taxi_zones_file_name)

    # percentile calculation
    quantile = df_trips_data.trip_distance.quantile(0.95)

    # Data filters: 1- Filter data with taxi zone greater than 263 (maximum zone ID); 2- Filter data with trip distance less than percentile 0,95 for trip distance
    df_filtered_data = df_trips_data[(df_trips_data['DOLocationID'] <= 263) & (df_trips_data['trip_distance'] > quantile)]

    # Iterate over filtered data to calculate number of trip drop-off inside each zone
    for index, row in df_filtered_data.iterrows():
        if row.DOLocationID not in DOLocationID_dict:
            DOLocationID_dict[row.DOLocationID] = 1

        elif row.DOLocationID in DOLocationID_dict:
            DOLocationID_dict[row.DOLocationID] = DOLocationID_dict[row.DOLocationID] + 1

    # Sort number of trips in each zone by descendent order
    sorted_DOLocationID_dict = sorted(DOLocationID_dict.items(), key=operator.itemgetter(1), reverse=True)

    # Iterate over 10 zones with most trips
    for item in sorted_DOLocationID_dict[:10]:
        # Getting info about borough, zone and number of trips
        location_id = item[0]
        trips_number = item[1]
        end_borough = df_taxi_zones[df_taxi_zones.LocationID == location_id].borough.tolist() # Get borough that matches with trip drop-off location ID
        end_zone = df_taxi_zones[df_taxi_zones.LocationID == location_id].zone.tolist() # Get zone that matches with trip drop-off location ID

        # Add data to separate lists
        trips_list.append(trips_number)
        borough_list.append(' '.join(end_borough))
        zone_list.append(' '.join(end_zone))

    # Put result data in correct format and convert it into a DataFrame
    results = {'Trips': trips_list,
               'end_borough': borough_list,
               'end_zone': zone_list}
    df_results = pd.DataFrame(results)  #

    return df_results


def print_result(result):
    # Print result data in OS terminal
    print(result)


def save_result(result, result_file_name):
    # Generate csv file with result data to save it
    result.to_csv(result_file_name, index=False)



if __name__== "__main__":

    if len(sys.argv) != 4:
        print("Argument number incorrect")
        print("First argument: Input data filname")
        print("Second argument: Taxi zones filename")
        print("Third argument: Result data filename")
        exit(0)

    #Read input arguments
    file_name = str(sys.argv[1])
    taxi_zones_file_name = str(sys.argv[2])
    result_file_name= str(sys.argv[3])

    result = process_data(file_name, taxi_zones_file_name)
    print_result(result)
    save_result(result, result_file_name)