import json
import urllib.request
import urllib

TOKEN = "<YOUR TOKEN GOES HERE>"
URL = "https://permagame.app.norsys.io/api"
STATE_PATH = "/state"
ACTION_PATH = "/action"
ACTION_LIST_PATH = "/actionList"
FAMILIES_PATH = '/plantFamilies'
PLANT_TYPES_PATH = '/plants'


def _fetchAndParseData(url):
    return json.loads(urllib.request.urlopen(url).read())

def fetchPlantTypes():
    return _fetchAndParseData(URL + PLANT_TYPES_PATH)

def fetchPlantFamilies():
    return _fetchAndParseData(URL + FAMILIES_PATH)

def fetchState():
    return _fetchAndParseData(URL + STATE_PATH)

def fetchGarden():
    data = fetchState()
    garden = data['garden']
    return garden

def fetchAllActions():
    return _fetchAndParseData(URL + ACTION_LIST_PATH)


def _postActionData(data):
    data = json.dumps(data).encode('utf8')
    req = urllib.request.Request(URL + ACTION_PATH, data=data,
                             headers={'content-type': 'application/json', 'Authorization': 'Bearer '+ TOKEN})
    try:
        urllib.request.urlopen(req)
        
    except urllib.error.HTTPError as e:
        res = json.load(e)
        print(res)


def plant(line, column, plantType):
    data = {'action':'plant', 'line':line, 'column':column, 'plantType': plantType}
    _postActionData(data)
    
def harvest(line, column):
    data = {'action': 'harvest', 'line': line, 'column': column}
    _postActionData(data)

def fertilize(line, column):
    data = {'action': 'fertilize', 'line': line, 'column': column}
    _postActionData(data)