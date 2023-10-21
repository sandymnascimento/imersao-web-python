#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """
    def __str__(self):
        html_entities = {
            "<": "&lt;",
            ">": "&gt;",
            "&": "&amp;",
            "\"": "&quot;"
        }
        if super().__str__() in html_entities:
            return super().__str__().replace(super().__str__(), html_entities[super().__str__()])
        else:
            return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self, value='incorrect behaviour.'):
            super().__init__(value)
    
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag 
        self.attr = attr
        self.tag_type = tag_type
        if content != None and not Elem.check_type(content):
            raise(Elem.ValidationError)
        else:
            self.content = content


    def __str__(self, nivel=0):
        """
        The __str__() method will permit us to make a plain HTML representation of our elements.
        """
        espacos = '  ' * nivel
        
        if self.tag_type == 'simple':
            if self.attr:
                result = f'<{self.tag} {self.__make_attr()}>' 
            else:
                result = f'<{self.tag}>'
        elif self.tag_type == 'double':
            if  self.attr and self.content:
                result = f'<{self.tag} {self.__make_attr()}>{self.__make_content()}</{self.tag}>' 

            elif self.attr:
                result = f'<{self.tag} {self.__make_attr()}></{self.tag}>'

            elif isinstance(self.content, Text):
                result = f'{espacos}<{self.tag}>\n{espacos}  {self.content.__str__()}\n{espacos}</{self.tag}>'    

            elif isinstance(self.content, Elem):
                content_str = self.content.__str__(nivel + 1)
                result = f'{espacos}<{self.tag}>\n{content_str}\n{espacos}</{self.tag}>'

            elif self.content:
                result = f'<{self.tag}>{self.__make_content()}</{self.tag}>'

            else:
                if nivel > 0:
                    result = f'{espacos}<{self.tag}></{self.tag}>'
                else:
                    result = f'<{self.tag}></{self.tag}>'

        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        try:
            if len(self.content) == 0:
                return ''
            result = '\n'
            for elem in self.content:
                if elem == '':
                    continue
                result += f'  {elem}\n'
            if result == '\n':
                return ''
            return result
        except:
            raise(Elem.ValidationError)

    def add_content(self, content):
        if not Elem.check_type(content):
            raise(Elem.ValidationError)
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

    
if __name__ == '__main__':
    img = Elem('img', {'src': 'http://www.python.org'}, tag_type='simple')
    head = Elem(tag=Text('head'),content=Elem(tag=Text('title'),content=Text('Hello ground!')))
    body = Elem(tag=Text('body'),content=[Elem(tag=Text('h1'),content=Text('Oh no, not again!')), img])
    print(str(Elem(tag=Text('html'),content=[head, body])))