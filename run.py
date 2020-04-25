from urllib.request import urlopen
from pprint import pprint
import json

baseUrl = "https://redive.estertion.win/spine/"

def get(url):
   return urlopen(baseUrl + url)
u = get('classMap.json')
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)