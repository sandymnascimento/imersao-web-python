import sys
import dewiki
import requests

def make_request(params, lang):
    url = f'http://{lang}.wikipedia.org/w/api.php'

    r = requests.get(url=url, params=params)
    
    response_text = r.text
    
    start = response_text.find('{')
    response_json = response_text[start:]
    response_dict = eval(response_json)

    return response_dict

def names(query, lang='en'):
    search_params = {
        'format' : 'json',
        'action' : 'query',
        'list' : 'search',
        'utf8': 1,
        'srlimit': 5,
        'srinfo' : 'suggestion',
        'srsearch': query
    }

    raw_results = make_request(search_params, lang)

    search_results = []
    for result in raw_results.get('query', {}).get('search', []):
        search_results.append(result['title'])

    searchinfo = raw_results.get('query', {}).get('searchinfo', {})
    return search_results, searchinfo.get('suggestion')


def search(title, lang='en', auto_suggest=True):
    name = title.replace(' ', '_').lower()
    title = title.title()
    
    if auto_suggest:
        results, suggestion = names(title, lang)

        if results:
            title = results[0].title()
        else:
            title = suggestion.title()
        
    query_params = {
        'action': 'query',
        'format' : 'json',
        'prop': 'extracts|revisions',
        'explaintext': '',
        'rvprop': 'ids',
        'titles': title
    }

    request = make_request(query_params, lang)

    try:
        query = request.get('query', {})
        pages = query.get('pages', {})
        pageid = list(pages.keys())[0]

        if not pages[pageid]['extract'] == '':
            result= open(f'{name}.wiki', 'w')
            result.write(dewiki.from_string(pages[pageid]['extract']))
            print('O arquivo com o conteúdo da requisição foi gerado.')
        else:
            raise(Exception)
    except Exception as ex:
        print('A requisição não apresentou resultados.')

def main():
    if len(sys.argv) == 2:
        search(sys.argv[1])
    elif len(sys.argv) == 3:
        search(sys.argv[1], sys.argv[2])
    else:
        print('Necessário informar o que deseja buscar.')

if __name__ == '__main__':
    main()


        
