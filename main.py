import requests
import json
import time
from datetime import datetime

API_KEY = "4eebb0d047c7f0ef4e8fc52bbd87323f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error:Unable to fetch weather data.")
        return None

def main():
    global date_time
    while True:
        print("*-WEATHER CHECKING APPLICATION-*:- \n")
        print("1. Check Weather by City Name")
        print("2. Add City to Favorites")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input("Enter your city name: ")
            weather_data = get_weather(city_name)
            if weather_data:
                temp_city = weather_data['main']['temp']
                weather_desc = weather_data['weather'][0]['description']
                hmdt = weather_data['main']['humidity']
                wind_spd = weather_data['wind']['speed']
                date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

                print("------------------------------------------------------------")
                print("Weather starts for - {} | {} ". format(city_name.upper(), date_time))
                print("------------------------------------------------------------")

                print("Current Temperature is: {:.2f} deg C".format(temp_city))
                print("Current Weather desc  :", weather_desc)
                print("Current Humidity      :", hmdt, '%')
                print("Current Wind Speed    :", wind_spd, 'kmph')
                print("------------------------------------------------------------\n")

        elif choice == "2":
            list = []
            favourite_city = int(input("Enter the total number of favourite cities: "))
            for i in range(0,favourite_city):
                ele = str(input())
                if ele not in list:
                    list.append(ele)
            print(f"{list} are the list of  your favourite cities.")
            break

        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid Choice. Please try again.")
        time.sleep(15 + 15 * (hash(city_name) % 2))

if __name__ == "__main__":
    main()
