import teolib
import csv


file_TipoAlloggi = "Codici_TipoAlloggiato.csv"

def TipoAlloggio(APIfield):
    with open(file_TipoAlloggi) as csvfile:
        reader = csv.reader(csvfile, delimiter=':')
        for row in reader:
            if row[0] == APIfield:
                return row[1]

def DataArrivo(APIfield):


def lengthcheck(str):
    print(str)
    print(len(str))


string = TipoAlloggio('FA')
lengthcheck(string)