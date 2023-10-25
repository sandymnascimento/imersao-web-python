#!/usr/bin/env python3
 
import sys
import json
import requests
import dewiki

import wikipedia 

def search_wiki(busca):
    url = "https://en.wikipedia.org/w/api.php"
    '''
    parametros = {
        "action": "query",
        "format": "json",
        'titles': busca,
        "prop": "extracts",
        "exintro": True,
        "plaintext": True
    }
    '''

    parametros = {
        "action": "query",
        "format": "json",
        'titles': busca,
        "prop": "extracts",
        "exintro": True,
        "plaintext": True
    }

    response = requests.get(url=url, params=parametros)

    if response.status_code != 200:
        return None
    
    print(response)

    data = response.json()
    

    page = next(iter(data['query']['pages'].values()))
    
    print(page['extract'].replace('</p><p>', '\n'))
    x = busca.replace(' ', '_')
    result= open(f'{x}.html', 'w')
    result.write(page['extract'])

    '''
    
    article_extract = response_json["query"]["pages"][0]["extract"]

    article_text = dewiki.remove_wiki_markup(article_extract)

    print(article_text)
'''

def main():
    #adicionar opção de escolher o idioma
    if len(sys.argv) == 2:
        search_wiki(sys.argv[1])

if __name__ == '__main__':
    main()

     '''
    @property
  def content(self):
    '''
 #   Plain text content of the page, excluding images, tables, and other data.
    '''

    if not getattr(self, '_content', False):
      query_params = {
        'prop': 'extracts|revisions',
        'explaintext': '',
        'rvprop': 'ids'
      }
      if not getattr(self, 'title', None) is None:
         query_params['titles'] = self.title
      else:
         query_params['pageids'] = self.pageid
      request = _wiki_request(query_params)
      self._content     = request['query']['pages'][self.pageid]['extract']
      self._revision_id = request['query']['pages'][self.pageid]['revisions'][0]['revid']
      self._parent_id   = request['query']['pages'][self.pageid]['revisions'][0]['parentid']

    return self._content
     '''