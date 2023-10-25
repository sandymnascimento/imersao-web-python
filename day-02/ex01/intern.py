class Intern:
    class Coffee:
        @staticmethod
        def __str__():
            return 'This is the worst coffee you ever tasted.'

    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'):
        self.name = name

    def __str__(self):
        return self.name

    def make_coffee(self):
        return Intern.Coffee()

    def work(self):
        try:
            raise(Exception('I’m just an intern, I can’t do that...'))
        except Exception as ex:
            print(f'{str(ex)}')         

def main():
    mark = Intern('Mark')
    print(mark.__str__())
    print(mark.make_coffee())

    estag = Intern()
    print(estag.__str__())
    estag.work()

if __name__ == '__main__':        
    main()