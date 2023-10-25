class HotBeverage:
    def __init__(self):
        self.name = 'hot beverage'
        self.price = 0.30
    
    def __str__(self) -> str:
        return f'name : {self.name} \nprice : {self.price} \ndescription : {self.description()}'

    def description(self):
        return 'Just some hot water in a cup.'
    
class Coffee(HotBeverage):
    def __init__(self):
        self.name = 'coffee'
        self.price = 0.40
        
    def description(self):
        return 'A coffee, to stay awake.'

class Tea(HotBeverage):
    def __init__(self):
        self.name = 'tea'
        self.price = 0.30
        
    def description(self):
        return 'Just some hot water in a cup.'

class Chocolate(HotBeverage):
    def __init__(self):
        self.name = 'chocolate'
        self.price = 0.50
        
    def description(self):
        return 'Chocolate, sweet chocolate...'

class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = 'cappuccino'
        self.price = 0.45
        
    def description(self):
        return 'Un po’ di Italia nella sua tazza!'

def main():
    print(HotBeverage().__str__())
    print(Coffee().__str__())

    tea = Tea()
    print(tea.__str__())

    drink = Chocolate()
    print(drink.__str__())

    print(Cappuccino().__str__())

if __name__ == '__main__':
    main()