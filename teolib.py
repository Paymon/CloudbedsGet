import json
import os.path
from urllib import request

def file(filename, text):
    if os.path.isfile(filename):
        f = open(filename, 'a')
    else:
        f = open(filename, 'w')
    f.write(text)
    f.close()

def get_json(url):
    with request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))