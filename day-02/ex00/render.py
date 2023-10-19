import sys
import os 
import re
import settings as sett


def open_file(arq):
    #Checar se existe o template e o settings antes de abrir, lançar erros.
    with open(arq, 'r') as template, open('cv.html', 'w') as cv:
        template = template.read()

        for model, value in sett.substituicoes.items():
            template = re.sub(model, value, template)
        cv.write(template)
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        open_file(sys.argv[1])