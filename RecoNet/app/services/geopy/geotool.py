from geopy import Nominatim
from geopy.distance import geodesic

class GeoTool:
    def __init__(self,user_agent="geo_tool_app"):
        self.geolocator = Nominatim(user_agent=user_agent,timeout=10)
        
    def get_coordinates(self,place_name):
        location = self.geolocator.geocode(place_name)
        if location:
            return {
                "address": location.address,
                "latitude": location.latitude,
                "longitude": location.longitude
            }
        return None
    
    def reverse_lookup(self,latitude,longitude):
        location = self.geolocator.reverse((latitude,longitude))
        if location:
            return location.address
        return None
    
    def get_distance_by_name(self,city1,city2):
        loc1 = self.geolocator.geocode(city1)
        loc2 = self.geolocator.geocode(city2)
        if loc1 and loc2:
            coordinate1 = (loc1.latitude,loc1.longitude)
            coordinate2 = (loc2.latitude,loc2.longitude)
            return geodesic(coordinate1,coordinate2).km
        return None
    
    def get_city_from_coords(self,latitude,longitude):
        location  = self.geolocator.reverse((latitude,longitude),language='en')
        if location:
            address = location.raw['address']
            return address.get('city') or address.get('town') or address.get('village')
        return None
    
    def get_distance_by_coords(self, lat1, lon1, lat2, lon2):
        coord1 = (lat1, lon1)
        coord2 = (lat2, lon2)
        return geodesic(coord1, coord2).km