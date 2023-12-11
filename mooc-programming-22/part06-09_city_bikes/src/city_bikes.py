# tee ratkaisu tänne
# Write your solution here
import math 

def get_station_data(filename: str):
    this_dct = {}

    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(';')

            if parts[0] == "Longitude": 
                continue

            this_dct[parts[3]] = (float(parts[0]), float(parts[1])) 
    
    return this_dct

def distance(stations: dict, station1: str, station2: str): 
    #print("stations[station1][0]", stations[station1][0])
    #print("stations[station1][1]", (stations[station1][1]))

    x_km = ((stations[station1][0]) - (stations[station2][0])) * 55.26
    y_km = ((stations[station1][1]) - (stations[station2][1])) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict) -> tuple: 
    this_dct = {} 
    max_dist = 0.0
    for stationOne in stations:
        for stationTwo in stations: 
            dist = distance(stations, stationOne, stationTwo)
            if dist > max_dist:
                max_dist = dist
                this_dct[max_dist] = (stationOne, stationTwo)

    return (this_dct[max_dist][0], this_dct[max_dist][1], max_dist)



    

if __name__ == "__main__":

    stations = get_station_data(r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part06-09_city_bikes\src\stations1.csv")
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

    """
    Longitude;Latitude;FID;name;total_slot;operative;id
    24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
    24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
    24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
    """