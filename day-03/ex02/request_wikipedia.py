import sys
import json
import requests
'''
request = requests.get()
    todo = json.loads(request.content)
    print(todo)
    print(todo['titulo'])
'''

def buscar_dados(busca):
    url = "https://fr.wikipedia.org/w/api.php"
    
    S = requests.Session()

    parametros = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": busca
    }

    R = S.get(url=url, params=parametros)
    DATA = R.json()
    print(DATA['query']['search'][0])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        buscar_dados(sys.argv[1])