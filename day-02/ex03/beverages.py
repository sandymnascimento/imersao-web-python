class HotBeverage:
    def __init__(self):
        self.name = 'hot beverage'
        self.price = 0.30
        self.descript = 'Just some hot water in a cup.'
    
    def __str__(self) -> str:
        return f'name : {self.name} \nprice : {self.price} \ndescription : {self.description()}'

    def description(self):
        return self.descript
    
class Coffee(HotBeverage):
    def __init__(self):
        self.name = 'coffee'
        self.price = 0.40
        self.descript = 'A coffee, to stay awake.'

class Tea(HotBeverage):
    def __init__(self):
        self.name = 'tea'
        self.price = 0.30
        self.descript = 'Just some hot water in a cup.'

class Chocolate(HotBeverage):
    def __init__(self):
        self.name = 'chocolate'
        self.price = 0.50
        self.descript = 'Chocolate, sweet chocolate...'

class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = 'cappuccino'
        self.price = 0.45
        self.descript = 'Un po’ di Italia nella sua tazza!'

if __name__ == '__main__':
    drink = Chocolate()
    print(drink.description())

    tea = Tea()
    print(tea.__str__())