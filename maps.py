import googlemaps
import googlemaps.geocoding
from typing import Tuple

google_maps_client: googlemaps.Client = googlemaps.Client(key = "AIzaSyD_ils9W_xYR9QAd5ZORGl8aF4pU0N4jTA")

def extract_address_coordinates(address: str) -> 'Tuple[float, float]':

    """
    Returns the latitude and longitude 
    of an address as a pair.
    """

    global google_maps_client

    location = googlemaps.geocoding.geocode(google_maps_client, address=address)    
    coordinates = location[0]["geometry"]["location"]

    return str(coordinates["lat"]), str(coordinates["lng"])

def map_link(address: str) -> str:

    coordinates = extract_address_coordinates(address)
    address_components = address.split(", ")

    for i in range(len(address_components)):
        address_components[i] = address_components[i].replace(" ", "+")

    formatted_address = ",".join(address_components)

    return "https://www.google.com/maps/embed/v1/search?key=AIzaSyD_ils9W_xYR9QAd5ZORGl8aF4pU0N4jTA&q=near+100&center=" + ",".join(coordinates)