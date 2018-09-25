from credentials_cimc import homerisk_credentials
import urllib3, requests, json

class homeRisk(object):

    def __init__(self, listvalues):

        headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=homerisk_credentials['username'], password=homerisk_credentials['password']))
        url = '{}/v3/identity/token'.format(homerisk_credentials['url'])
        response = requests.get(url, headers=headers)
        mltoken = json.loads(response.text).get('token')

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"fields":["House id", 'House orientation', 'Type of house', 'Topography', 'Drought', 'Access way', 'High-tension towers', 'Next the house', 'Fence', 'Water', 'Outer walls', 'Accumulation of leaves', 'Roof', 'Barbecue', 'Waterproof', 'Water source'],"values":
            [["House", int(listvalues[0]), int(listvalues[1]), int(listvalues[2]), int(listvalues[3]), int(listvalues[4]), int(listvalues[5]), int(listvalues[6]), int(listvalues[7]),
            int(listvalues[8]), int(listvalues[9]), int(listvalues[10]), int(listvalues[11]), int(listvalues[12]), int(listvalues[13]), int(listvalues[14])]]}

        response_scoring = requests.post(homerisk_credentials["call"], json=payload_scoring, headers=header)

        self.results = json.loads(response_scoring.text)

    def get_risk(self):
        l = len(self.results['values'][0])
        return str(self.results['values'][0][l-1])
