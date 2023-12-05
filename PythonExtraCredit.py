import requests
import json

def current_temp():
  print("Welcome! This program will tell you the current weather of the city you input!\n")
  city = input("Please enter the city name: ")
  
  api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c8efac34cc3548754ca009222d24da49&units=imperial"
  
  response = requests.get(api_url)
  responsejson = response.json()
  
  weather = responsejson['weather']
  conditions = weather[0]['main']
  description = weather[0]['description']
  
  degrees = responsejson['main']['temp']
  min_degrees = responsejson['main']['temp_min']
  max_degrees = responsejson['main']['temp_max']
  
  print()
  print(f"Here are the current weather conditions in {city}")
  print()
  print(f"Current Conditions: {conditions}")
  print(f"Description: {description}")
  print(f"Current temperature: {degrees} Fahrenheit")
  print(f"Low for today: {min_degrees} Fahrenheit")
  print(f"High for today: {max_degrees} Fahrenheit")
  
  if int(degrees) > 65:
    print()
    print("Short sleeve weather!")
  else:
    print()
    print("Long sleeve weather!")

current_temp()



