from elements import *

class Page:
    def __init__(self, elem) -> None:
        self.elem = elem
        

    def is_valid(self):
        print(self.elem.tag)
        for node in self.elem.content:
            if not self.check_tree(node):
                return False
        if self.elem.tag == 'html':
            if self.elem.content != [ Head(), Body() ]:
                print(self.elem.content)
        return True

    def check_tree(self, node):
        types = {'Html', 'Head', 'Body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br', 'text'}

        if node.__class__.__name__ not in types:
            return False
        if node.content:
            for content_node in node.content:
                if not self.check_tree(content_node):
                    return False
        return True

    
    #def write_to_file(name):

if __name__ == '__main__':
    title = Title(content=Text('Hello ground!'))
    head = Head(title)
    img = Img({'src': 'http://www.python.org'})
    h1 = H1(content=Text('Oh no, not again!'))

    th1 = Th(content=Text('Name'))
    th2 = Th(content=Text('Cups'))
    td1 = Td(content=Text('JAmes'))
    td2 = Td(content=Text('10'))
    tr1 = Tr(content=[th1, th2])
    tr2 = Tr(content=[td1, td2])
    table = Table(content=[tr1, tr2])

    body = Body([h1, img])
    ins = Page( Html( [Head(), Body()] ) )
    print(ins.is_valid())
    #print( Html( [head, body] ) )
    #print( Html( [Head(), Body()]))