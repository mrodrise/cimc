import urllib3, requests, json

from credentials_cimc import fireload_credentials

class fireLoad(object):

    def __init__(self, data_list):
        activity_ra = {"Footwear": 1,
        "Supply, packaging" :1.5,
        "Cardboard": 1.5,
        "Wood goods, carpentry": 1.5,
        "Synthetic goods": 2}

        headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=fireload_credentials['username'], password=fireload_credentials['password']))
        url = '{}/v3/identity/token'.format(fireload_credentials['url'])
        response = requests.get(url, headers=headers)
        mltoken = json.loads(response.text).get('token')

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line

        print ("fireLoad - lista que se entrega en la llamada a Watson")
        print(["House1", data_list[1], activity_ra[data_list[0]], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7]])

        payload_scoring = {"fields":["House id", "Area", "Activity Ra", "Product1", "Product2", "Product3", "Product4", "Product5", "Other products"],
            "values":[["House1", float(data_list[1]), activity_ra[data_list[0]], float(data_list[2]),
            float(data_list[3]), float(data_list[4]), float(data_list[5]), float(data_list[6]), float(data_list[7])]]}

        response_scoring = requests.post(fireload_credentials["call"], json=payload_scoring, headers=header)
        self.results = json.loads(response_scoring.text)


    def get_fire_load(self):
        print ("get_fire_load - imprimo los resultados de la llamada a Watson")
        print (str(self.results))
        print (str(self.results['values'][0]))
        print (str(self.results['values'][0][10]))
        return str(self.results['values'][0][10])
