import sys
import json
import dewiki
import requests

def make_request(params, lang):
    url = f'http://{lang}.wikipedia.org/w/api.php'

    r = requests.get(url=url, params=params)
    
    if r.status_code != 200:
        print('A requisição não retornou o resultado esperado.')

    response_text = r.text
    
    json_start = response_text.find('{')
    response_json = response_text[json_start:]
    response_dict = eval(response_json)

    return response_dict

def search(query, lang='en', suggestion=True):
    search_params = {
        'format' : 'json',
        'action': 'query',
        'list': 'search',
        'utf8':1,
        'srlimit':5,
        'srsearch': query
    }
    if suggestion:
        search_params['srinfo'] = 'suggestion'

    raw_results = make_request(search_params, lang)

     # Analisar manualmente os resultados
    search_results = []
    for result in raw_results.get('query', {}).get('search', []):
        search_results.append(result['title'])

    if suggestion:
        searchinfo = raw_results.get('query', {}).get('searchinfo', {})
        return search_results, searchinfo.get('suggestion')

    return search_results, None

def page(title=None, lang='en', auto_suggest=True):
    if title is not None:
        name = title
        title = title.title()
        
        if auto_suggest:
            results, suggestion = search(title, lang)

            if results:
                title = results[0]
            else:
                title = suggestion
         
        query_params = {
            'action': 'query',
            'format' : 'json',
            'prop': 'extracts|revisions',
            'explaintext': '',
            'rvprop': 'ids',
            'titles': title
        }

        request = make_request(query_params, lang)
        print(request)
        try:
            query = request.get('query', {})
            pages = query.get('pages', {})
            pageid = list(pages.keys())[0]

            x = name.replace(' ', '_')
            result= open(f'{x}.html', 'w')
            result.write(dewiki.from_string(pages[pageid]['extract']))
            print('O arquivo com o conteúdo da requisição foi gerado.')
        except Exception as ex:
            print('A requisição não apresentou resultados.')


def main():
    #adicionar opção de escolher o idioma
    if len(sys.argv) == 2:
        page(sys.argv[1])
    elif len(sys.argv) == 3:
        page(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
    main()


        
