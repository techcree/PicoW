#by StSkanta (TechCree) 838375
import requests
import json
from apikey import api_key

#api_key information is in apikey.py

city_name = "Hamburg"
city_value = city_name

weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

response = requests.get(weather_url)
data = json.loads(response.text)

#test data output enable print(data)
#print(data)

weather_info = data

# changing response from json to python readable 
weather_info = response.json()
 
 
#tfield.delete("1.0", "end")   #to clear the text field for every new output
 
        
if weather_info['cod'] == 200:
    kelvin = 273 # Umrechnung kelvin zu Celsius

#Daten lesbar und Variablen
 
temp = int(weather_info['main']['temp'] - kelvin)     #kelvin value zu Celcius
feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
pressure = weather_info['main']['pressure']
humidity = weather_info['main']['humidity']
wind_speed = weather_info['wind']['speed'] * 3.6
sunrise = weather_info['sys']['sunrise']
sunset = weather_info['sys']['sunset']
timezone = weather_info['timezone']
cloudy = weather_info['clouds']['all']
description = weather_info['weather'][0]['description']
#sunrise_time = time_format_for_location(sunrise + timezone)
#sunset_time = time_format_for_location(sunset + timezone)

weather = f"\nHeute in: {city_name}\nTemperatur (Celsius): {temp}°\ngefühlt (Celsius): {feels_like_temp}°\nLuftdruck: {pressure} hPa\nFeuchtigkeit: {humidity}\nBewölung: {cloudy}%\nHimmel: {description}"
print(weather)