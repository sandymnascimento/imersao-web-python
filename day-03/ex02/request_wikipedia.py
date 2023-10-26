import sys
import json
import dewiki
import requests

def _wiki_request(params):
    params['format'] = 'json'
    if not 'action' in params:
        params['action'] = 'query'

    r = requests.get('http://en.wikipedia.org/w/api.php', params=params)

    return r.json()

def search(query, results=10, suggestion=False):
    search_params = {
        'list': 'search',
        'srprop': '',
        'srlimit': results,
        'limit': results,
        'srsearch': query
    }
    if suggestion:
        search_params['srinfo'] = 'suggestion'

    raw_results = _wiki_request(search_params)

    search_results = (d['title'] for d in raw_results['query']['search'])

    if suggestion:
        if raw_results['query'].get('searchinfo'):
            return list(search_results), raw_results['query']['searchinfo']['suggestion']
        else:
            return list(search_results), None

    return list(search_results)

def page(title=None, auto_suggest=True):
    if title is not None:
        if auto_suggest:
            results, suggestion = search(title, results=1, suggestion=True)
            title = suggestion or results[0]
        query_params = {
            'prop': 'extracts|revisions',
            'explaintext': '',
            'rvprop': 'ids'
        }
        query_params['titles'] = title

        request = _wiki_request(query_params)
        query = request['query']
        pageid = list(query['pages'].keys())[0]

        x = title.replace(' ', '_')
        result= open(f'{x}.wiki', 'w')
        result.write(request['query']['pages'][pageid]['extract'])


def main():
    #adicionar opção de escolher o idioma
    if len(sys.argv) == 2:
        page(sys.argv[1])

if __name__ == '__main__':
    main()


        
