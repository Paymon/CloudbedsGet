import teolib
import json
from pprint import pprint



filename = "MBPC0000.DAT"


print("... importazione prenotazioni ...")


urlapi = "https://hotels.cloudbeds.com/api/getReservationArrivals"
fromdate = "2016-06-06"
todate = "2016-06-06"

print (urlapi + "?resultsFrom=" + fromdate + "&resultsTo=" + todate)

reservation = teolib.get_json(urlapi + "?resultsFrom=" + fromdate + "&resultsTo=" + todate)

nrecord = len(reservation['data'])
print(" sono stati importati record : ", nrecord)

for rec in reservation['data']:
    print(rec['reservationID'])
    print ("https://hotels.cloudbeds.com/api/getReservation?reservationID=" + rec['reservationID'])
    invoice = teolib.get_json("https://hotels.cloudbeds.com/api/getReservation?reservationID=" + rec['reservationID'])
    pprint (invoice['data'])


    #pprint(invoice)

    #print(parsed_json['data'])

#file(filename, json.dumps(parsed_json))