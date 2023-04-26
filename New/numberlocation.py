import phonenumbers
from geopy.geocoders import Nominatim
from home_page import SignupPage
from phonenumbers import geocoder



def track():

        Key="29bb9fad6b8549c6b393379e37b67ec3"
        
        sanNumber = phonenumbers.parse(SignupPage.entry_phone)

        yourLocation=geocoder.description_for_number(sanNumber, "en")
        print(yourLocation)
        geolocator = Nominatim(user_agent="geoapiExercises")
        from opencage.geocoder import OpenCageGeocode
        geocoder=OpenCageGeocode(Key)

        query=str(yourLocation)
        results=geocoder.geocode(query)
        #print(results)

        lat=results[0]['geometry']['lat']
        lng=results[0]['geometry']['lng']
        location = geolocator.geocode(str(lat) + "," + str(lng))
        print(location)
