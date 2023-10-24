import sys

def get_state(state):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    if state in states:
      return states[state]
    else:
      return "N/A"

def get_cities(sigla):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
   
    return capital_cities[sigla] 

def search(state):
    sigla = get_state(state)    
    if sigla != "N/A":
        print(get_cities(sigla)) 
    else:
        check = get_state(state.split(' ')[0])
        if check == "N/A":            
            print('Unknown state')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        search(sys.argv[1])
    elif len(sys.argv)  == 3:
        search(sys.argv[1] + " " + sys.argv[2])
