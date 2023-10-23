import sys

def get_cities(capital):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    for sigla, cap in capital_cities.items():
        if cap == capital:
            return sigla
    return 'N/A'

def get_state(sigla):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    for state, sig in states.items():
        if sig == sigla:
            return state

def search(capital):
    sigla = get_cities(capital) 
    if sigla != 'N/A':
        print(get_state(sigla))
    else:
        print('Unknown capital city')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        search(sys.argv[1])
    else:
        print('Unknown state')