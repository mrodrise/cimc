import googlemaps
from datetime import datetime
from credentials_cimc import key_googlemaps

class mapRoute(object):

    def __init__(self, origin, destination):
        self.gmaps = googlemaps.Client(key=key_googlemaps)
        self.origin = origin
        self.destination = destination

    def get_duration(self):
        now = datetime.now()
        directions_result = self.gmaps.directions(self.origin, self.destination, mode="driving", departure_time=now)
        print(directions_result[0]['legs'][0]['duration']['value'])
        return(directions_result[0]['legs'][0]['duration']['value'])
