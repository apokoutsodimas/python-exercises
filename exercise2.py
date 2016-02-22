import json
import requests
import sys

def main():
    #security issues enter the api key (sign up on openweathermap")
    apikey = raw_input("Please enter your api key for openweathermap application: ")
    if not apikey:
        print "Invalid api key"
        sys.exit()
    #prompt user for latitude
    latitude = raw_input("Please enter the latitude: ")
    #check is not empty
    if not latitude:
        print "Invalid latitude"
        sys.exit()
    #prompt user for longitude
    longitude = raw_input("Please enter the longitude: ")
    #check if empty
    if not latitude:
        print "Invalid longitude"
        sys.exit()
    #construct rest request
    r=requests.get("http://api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&units=metric&appid="+apikey)
    #check for Success http code
    if (r.ok):
        current_weather = json.loads(r.content)
        if current_weather['weather'][0]['main']=="Rain":
            print "i am singing in the rain"
        if (current_weather['main']['temp']>20):
            print "nice"
        elif (current_weather['main']['temp']<5):
            print "brrrrr"
    else:
        print "Invalid request"

if __name__ == '__main__':
    main()