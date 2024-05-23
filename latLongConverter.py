from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import pandas as pd

df = pd.read_csv("ReDU_filtered_file.tsv", sep='\t')

list_of_coordinates: list[str] = df['LatitudeandLongitude'].tolist()

unique_coordinates: set[str] = set(list_of_coordinates)

unique_coordinates_list: list[str] = list(unique_coordinates)

def get_city_names(list_of_coordinates, retry_count=3):
    geolocator = Nominatim(user_agent="YourApplicationName")
    city_names = []
    for coordinates in list_of_coordinates:
        for i in range(retry_count):
            try:
                location = geolocator.reverse(coordinates, exactly_one=True)
                if location is None:
                    print(f"No location found for coordinates: {coordinates}")
                    break
                address = location.raw['address']
                city = address.get('city', '')
                city_names.append(city)
                break
            except GeocoderTimedOut:
                if i < retry_count - 1:
                    continue
                else:
                    raise
    return city_names

def parse_coordinates(coordinate_string):
    latitude, longitude = map(float, coordinate_string.replace(',', '|').replace(';', '|').split('|'))
    return [float(latitude), float(longitude)]

def parse_coordinate_list(list_of_coordinates):
    parsed_coordinates = []
    for coordinate_string in list_of_coordinates:
        if (coordinate_string != "not collected" and coordinate_string != "not specified" and coordinate_string != "" and coordinate_string != "not applicable" and coordinate_string != "ML import: not available"):
            coordinates = parse_coordinates(coordinate_string)
            if coordinates is not None:
                parsed_coordinates.append(parse_coordinates(coordinate_string))
    return parsed_coordinates

parsed_coordinate_list: list[list[float]] = parse_coordinate_list(unique_coordinates_list)

city_names = get_city_names(parsed_coordinate_list)

with open('city_names.txt', 'w', encoding='utf-8') as f:
    for city_name in city_names:
        f.write(city_name + '\n')
