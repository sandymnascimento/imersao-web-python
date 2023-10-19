import os 

def open_file():
    folder = os.getcwd()
    for name_file in os.listdir(folder):
        if os.path.isfile(name_file) and name_file.endswith('.txt'):
            with open(name_file, 'r') as arquivo:
                numbers =  arquivo.read()
                print(numbers.replace(",", "\n"))
            break

#with open(numbers.txt, 'r') as arquivo:

if __name__ == '__main__':
    open_file()