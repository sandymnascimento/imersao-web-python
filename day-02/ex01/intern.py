class Intern:
    class Coffee:
        @staticmethod
        def __str__():
            return 'This is the worst coffee you ever tasted.'

    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'):
        self.name = name

    def __str__(self):
        return self.name

    def work(self):
        raise('I’m just an intern, I can’t do that...')
    
    def make_coffee(self):
        return Intern.Coffee()
    
if __name__ == '__main__':        
    estag = Intern()
    print(estag.__str__())
    print(estag.make_coffee())

    mark = Intern("Mark")
    print(mark.__str__())
    
    #estag.work()