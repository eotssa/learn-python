# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, station_name: str) -> None:
        self.__station_name = station_name
        self.__observationList = []


    def add_observation(self, observation: str):
        self.__observationList.append(observation)
    
    def number_of_observations(self):
        return len(self.__observationList)

    def latest_observation(self):
        if self.number_of_observations() != 0:
            return self.__observationList[-1]
        else:
            return ""

    def __str__(self) -> str:
        return f"{self.__station_name}, {self.number_of_observations()} observations"    


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)