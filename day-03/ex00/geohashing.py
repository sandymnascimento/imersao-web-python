#!/usr/bin/env python3

import sys
import antigravity

def geohashing(latitude, longitude, date="2005-05-26", dow='10458.68'):
    date = f'{date}-{dow}'
    antigravity.geohash(latitude, longitude, date.encode())

def valida_valores(latitude, longitude):
    try:
        if -90 <= float(latitude) <= 90 and -180 <= float(longitude) <= 180:
            return True
        else:
            print(f"Valores informados fora do range esperado para latitude e longitude.")
            return False
    except ValueError:
        print("O valor deve permitir transformação para float. Exemplo: 10458.68")

def main():
    try:
        if len(sys.argv) == 3:
            if valida_valores(sys.argv[1], sys.argv[2]):
                geohashing(float(sys.argv[1]), float(sys.argv[2]))
        elif len(sys.argv) == 5:
            if valida_valores(sys.argv[1], sys.argv[2]):
                geohashing(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4])
        else:
            raise(ValueError)
        
    except ValueError as e:
        print('Número incorreto de argumentos. Argumentos necessários: latitude, longitude, date, cod')

    finally:
        sys.exit(1)

if __name__ == '__main__':    
    main()

#37.421542 -122.085589