from credentials_cimc import fireprobability_credentials
import urllib3, requests, json

class fireProbability(object):

    def __init__(self, weather):

        temperature = weather.get_temperature()
        humidity = weather.get_humidity()
        wind = weather.get_wind()

        headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=fireprobability_credentials['username'], password=fireprobability_credentials['password']))
        url = '{}/v3/identity/token'.format(fireprobability_credentials['url'])
        response = requests.get(url, headers=headers)
        mltoken = json.loads(response.text).get('token')

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        payload_scoring = {"fields":["Temperature", "Relative Humidity", "Wind Speed"],
            "values":[[float(temperature), float(humidity), float(wind)]]}

        response_scoring = requests.post(fireprobability_credentials["call"], json=payload_scoring, headers=header)
        self.results = json.loads(response_scoring.text)
        print("fireProbability - imprimo el valor de self.results")
        print(self.results)

    def get_fire_probability(self):
        print (str(self.results['values'][0]))
        print (str(self.results['values'][0][7]))
        return str(self.results['values'][0][7])
