import teolib

filename = "MBPC0000.DAT"


print("... importazione prenotazioni ...")


urlapi = "https://hotels.cloudbeds.com/api/getReservationArrivals"
fromdate = "2016-01-24"
todate = "2016-04-24"
reservation = teolib.get_json(urlapi + "?resultsFrom=" + fromdate + "&resultsTo=" + todate)

nrecord = len(reservation['data'])
print(" sono stati importati record : ", nrecord)

for rec in reservation['data']:
    print(rec['reservationID'])
    invoice = teolib.get_json("https://hotels.cloudbeds.com/api/getReservationInvoiceInformation?reservationID=" + rec['reservationID'])
    print(invoice['data'])

#print(parsed_json['data'])

#file(filename, json.dumps(parsed_json))