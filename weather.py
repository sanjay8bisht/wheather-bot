
from datetime import date, datetime
import sys
import time
import json
from config import *

def log(text):
    PY_VERSION = sys.version_info[0]

    if PY_VERSION == 2:
        print text

    if PY_VERSION == 3:
        print(text)


def get_response(url):
    PY_VERSION = sys.version_info[0]

    if PY_VERSION == 2:
        try:
            import urllib
            return json.loads(urllib.urlopen(url).read())
        except:
            raise Exception('try -> pip install urllib')

    if PY_VERSION == 3:
        try:
            import requests
            return json.loads(requests.get(url).text)
        except:
            raise Exception("try -> pip install requests")

    
def get_wheather(place):
    log("Retrieving new information")
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={key}".format(place=place,key=KEY)
    response = get_response(api_url)
    max_temp = int(response['main']['temp_max']) - 273
    min_temp = int(response['main']['temp_min']) -273
    result = """
    ======================================
    ||  Country : {country}             
    ||  Latitude : {lat}                
    ||  Longitude : {long}              
    ||  Whether : {weather}             
    ||  Min Temp : {min_temp}           
    ||  Max Temp : {max_temp}           
    ======================================""".format(country=response['sys']['country'],lat=response['coord']['lat'],long=response['coord']['lon'],
        weather=response['weather'][0]['main'],min_temp=min_temp,max_temp=max_temp)
    
    log(result)
   
            
if __name__=='__main__':
    place  = sys.argv[1]
    get_wheather(place)