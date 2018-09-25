from credentials_cimc import weather_credentials
import requests
import json

class actualWeather(object):

    def __init__(self, country_code, zip):

        watsonUrl = 'https://twcservice.eu-gb.mybluemix.net/api/weather/v1/location/' + zip + ':4:ES' + '/observations.json?language=es'

        r = requests.get(watsonUrl,auth=(weather_credentials["username"], weather_credentials["password"]))
        print ("actualWeather - ya he hecho el request al servicio de The Weather Company")
        self.results = json.loads(str(r.text))
        print ("actualWeather - el resultado de la llamada es")
        print (self.results)


    def get_temperature(self):
        return str(self.results['observation']['temp'])

    def get_humidity(self):
        return str(self.results['observation']['rh'])

    def get_wind(self):
        return str(self.results['observation']['wspd'])
