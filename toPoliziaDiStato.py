import teolib
import csv


file_TipoAlloggi = "Codici_TipoAlloggiato.csv"

def get_csv(APIfield, file):
#lunghezza 2 caratteri
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=':')
        for row in reader:
            if row[0] == APIfield.upper():
                return row[1]

def Data(APIfield):
#lunghezza 10 caratteri
    aaaa = APIfield[0:4]
    mm = APIfield[5:7]
    gg = APIfield[8:10]
    newdata = (gg + "/" + mm + "/" + aaaa)
    return newdata

def NGiorni(APIfield):
#lunghezza 2 caratteri
    gg = APIfield
    return gg

def Name(APIfield, length):
    name = APIfield
    for j in range(length - len(APIfield)):
        name += "."
    return name

def lengthcheck(str):
    print(str)
    print(len(str))


string = get_csv('fA', file_TipoAlloggi) + Data('2016/04/25') + NGiorni('01') + Name('Noris', 50) + Name('Matteo', 30) + 'm' + Data('1976/10/31')
lengthcheck(string)