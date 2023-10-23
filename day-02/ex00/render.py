import sys
import os 
import re
import settings as sett


def open_file(arq):
    folder = os.getcwd()     
    conteudo = os.listdir(folder)
    
    if arq in conteudo and 'settings.py' in conteudo:       
        with open(arq, 'r') as template, open('cv.html', 'w') as cv:
            template = template.read()

            substituicoes = {}
            with open('settings.py', 'r') as settings:
                for line in settings:
                    if '=' in line:
                        key, value = line.split('=')
                        substituicoes['{' + key.strip() + '}'] = value.strip()[1:-1]       

            for model, value in substituicoes.items():
                template = re.sub(model, value, template)
            cv.write(template)
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        open_file(sys.argv[1])