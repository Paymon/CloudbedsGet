import teolib
import datetime
import csv

fileroot = "c://"

crlf = chr(13) + chr(10)
vettore = []
file_TipoAlloggi = "Codici_TipoAlloggiato.csv"
file_CodiceComune = "Comuni.csv"
file_CodiceNazione = "Nazioni.csv"
file_CodiceDocumento = "Documenti.csv"

def get_csv(file, FieldIN, FieldOUT, APIfield):
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=':')
        for row in reader:
            if row[FieldIN] == APIfield.upper():
                return row[FieldOUT]


def Data(APIfield):
    aaaa = APIfield[0:4]
    mm = APIfield[5:7]
    gg = APIfield[8:10]
    newdata = (gg + "/" + mm + "/" + aaaa)
    return newdata


def NGiorni(APIfield):
    gg = APIfield
    return gg


def Name(APIfield, length):
    name = APIfield
    for j in range(length - len(APIfield)):
        name += " "
    return name


def CodComune(APIFieldNazione, APIFieldComune):
    if APIFieldNazione.upper() == "ITALIA":
        return get_csv(file_CodiceComune, 1, 0, APIFieldComune)
    else:
        return "         "


def CodProvincia(APIFieldNazione, APIFieldProvincia):
    if APIFieldNazione.upper() == "ITALIA":
        return APIFieldProvincia.upper()
    else:
        return "  "


def CodRilascio(APIFieldNazione, APIFieldComune):
    if APIFieldNazione.upper() == "ITALIA":
        return get_csv(file_CodiceComune, 1, 0, APIFieldComune.upper())
    else:
        return get_csv(file_CodiceNazione, 1, 0, APIFieldNazione.upper())


def lengthcheck(str):
    print(str)
    print(len(str))



TipoAlloggi = get_csv(file_TipoAlloggi,0,1,"FA")
DataArrivo = Data('2016/04/25')
NumeroGiorni = NGiorni('01')
Cognome = Name('Noris', 50)
Nome = Name('Matteo', 30)
Sesso = 'm'.upper()
DataNascita = Data('1976/10/31')
Comune = CodComune("ItALIA", "ALMESE")
Provincia = CodProvincia("Italia", "rm")
NazioneNascita = get_csv(file_CodiceNazione,1,0,"BHUTAN")
NazioneResidenza = get_csv(file_CodiceNazione,1,0,"ITaLIA")
TipoDocumento = get_csv(file_CodiceDocumento,1,0,"PASSAPORTO ORDINARIO")
NumeroDocumento = Name("1234567890", 20)
NazioneRilascio = CodRilascio("ITALIA", "ALMESE")


string = TipoAlloggi + DataArrivo + NumeroGiorni + Cognome + Nome + Sesso + DataNascita + Comune + Provincia + NazioneNascita + NazioneResidenza + TipoDocumento + NumeroDocumento + NazioneRilascio
lengthcheck(string)


for i in range(0,9):
    if i != 0:
        vettore.append(crlf + string)
    else:
        vettore.append(string)

print exportfilename = fileroot + "Alloggiati_" + datetime.datetime.now().strftime("%Y-%m-%d") + "txt"
#teolib.array2file(exportfilename, vettore)

#teolib.emailfile("","","",exportfilename)