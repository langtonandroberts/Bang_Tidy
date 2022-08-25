from doctest import script_from_examples
from unittest import result
import phonenumbers
from phonenumbers import carrier, region_code_for_country_code, region_code_for_number
from phonenumbers import geocoder
import folium

from pprint import pprint
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import OpenCageGeocode
from mynumber import number


samnumber=phonenumbers.parse(number)
print("The phone number being searched is: ",number)

yourLocation=geocoder.description_for_number(samnumber,"en")#,region="en")
print("The phone is alocated in: ",yourLocation)

service_provider=phonenumbers.parse(number)
print("The phone service provider is: ",carrier.name_for_number(service_provider,"en"))#,region="en"))

address_template=geocoder.parse(number)
print(address_template)


keyTomTom='JRXEx2LVw4GJYRkhOC0I9quuJth0IziP'#,,TOMTOM,,,key
key='045c5a7c88c245848e44b032a43923d2'#OpenCageCode,,,key
geocoder=OpenCageGeocode(key)
query=str(yourLocation)
results=geocoder.geocode(query)
print(results)

#lat=results[0]['geometry']['lat']
#lng=results[0]['geometry']['lng']
#print(lat,lng)
#print(results[0]['fprmatted'])

#myMap=folium.Map(location=[lat,lng],zoom_start=9)
#folium.Marker(lat,lng,popup=yourLocation).add_to(myMap)
#save map to html file
#myMap.save('myLocation.html')


