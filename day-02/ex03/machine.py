import random
import beverages

class CoffeeMachine:
    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            self.name = 'empty cup'
            self.price = 0.90
            self.descript = 'An empty cup?! Gimme my money back!'

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired.')

    def __init__(self) -> None:
        self.served = 0
        
    def repair(self):
        self.served = 0

    def serve(self, drink):
        try:
            if self.served < 10:
                opt = [drink, CoffeeMachine.EmptyCup()]
                serve = random.choice(opt)
                print(f'{serve.description()}')
                self.served+=1
            else:
                raise(CoffeeMachine.BrokenMachineException)
        except CoffeeMachine.BrokenMachineException as ex:
            print(f'{str(ex)}')
            self.repair()


if __name__ == '__main__':
    coffeemach = CoffeeMachine()
    for i in range(13):
        drinkOptions = [beverages.Coffee(), beverages.Chocolate(), beverages.Cappuccino(), beverages.Tea()]
        choose = random.choice(drinkOptions)
        coffeemach.serve(choose)
