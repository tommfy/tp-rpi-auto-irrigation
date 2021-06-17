import os
import sys
import requests
import ConfigParser
import datetime
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat=51.37610581678528&lon=0.44608559709327733&appid=886705b4c1182eb1c69f28eb8c520e20"
# HTTP request
response = requests.get(BASE_URL)


# OR USE CITY
#BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#City Name CITY = "London"
#API key API_KEY = "Your API Key"
#URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY


# Checking the status code of the request
# Test API access
if response.status_code == 200:

   # getting data in the json format
   data = response.json()
   # weather report
   report = data['weather']
   print(f"Weather Report: {report[0]['main']}")

   rainstatus = (f"Weather Report: {report[0]['main']}")

else:
   # showing the error message
   print("Error connecting to API")


  # If rain then run sprinkler

   # if report not in ['rain', 'shower rain', 'thunderstorm', 'snow', 'Rain', 'Shower Rain', 'Thunderstorm', 'Snow', 'Shower rain', 'Thunder storm', 'Thunder Storm']:
     # run_sprinkler(config)
     # print "Success! No Rain"
