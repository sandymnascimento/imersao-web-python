import sys

def states():
    return {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

def capital_cities():
    return {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

def search(names):
    list_names = names.split(',')
    for string in list_names:
        stop = True
        if string == ' ':
            continue

        name = string.strip().title()
        
        if name in states():
            print(f'{capital_cities()[states()[name]]} is the capital of {name}')
            continue
        else:
            for sigla, cap in capital_cities().items():
                if cap == name:
                    for state, sig in states().items():
                        if sig == sigla:
                            print(f'{name} is the capital of {state}')
                            stop = False
                            break
                    break
        if stop:
            if string != '':
                print(f'{string.strip()} is neither a capital city nor a state')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        search(sys.argv[1])
    else:
        print('Unknown state')