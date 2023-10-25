import sys
import json
import requests
import dewiki

def search_wiki(busca):
    url = "https://fr.wikipedia.org/w/api.php"
    parametros = {
        "action": "query",
        "format": "json",
        "list": "search",
        "prop": "extracts",
        "srsearch": busca
    }

    response = requests.get(url=url, params=parametros)

    if response.status_code != 200:
        return None

    response_json = json.loads(response.content)
    print(response_json)
    article_extract = response_json["query"]["pages"][0]["extract"]

    article_text = dewiki.remove_wiki_markup(article_extract)

    print(article_text)

def main():
    #adicionar opção de escolher o idioma
    if len(sys.argv) == 2:
        search_wiki(sys.argv[1])

if __name__ == '__main__':
    main()