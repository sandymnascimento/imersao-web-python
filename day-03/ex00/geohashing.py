import sys
import antigravity

def geohashing(latitude, longitude, date="2005-05-26-10458.68"):
  print(antigravity.geohash(latitude, longitude, date.encode()))

def main():
    try:
        if len(sys.argv) == 2:
            geohashing(float(sys.argv[1]), float(sys.argv[2]))
        elif len(sys.argv) == 3:
           geohashing(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3])
    except ValueError as e:
        print(e)
        sys.exit(1)
if __name__ == '__main__':    
    main()

#37.421542 -122.085589