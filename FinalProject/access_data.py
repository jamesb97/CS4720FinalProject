'''
Python program for displaying the current weather reports in a JSON format
'''
import requests

from pprint import pprint
API_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter City Name: ")
Final_url = base_url + "appid=" + API_KEY + "&q=" + city_name

weather_data = requests.get(Final_url).json()

print("\nCurrent Weather Data Of: " + city_name + ":\n")
pprint(weather_data)

