#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    class ValidationError(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired.')
    """
    Elem will permit us to represent our HTML elements.
    """

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag 
        self.attr = attr
        self.tag_type = tag_type
        self.content = content

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':

            if  self.attr != {} and self.content:
                result = f'<{self.tag} {self.attr}>{self.content}</{self.tag}>' 
            elif self.attr != {}:
                result = f'<{self.tag} {self.attr}></{self.tag}>'
            elif type(self.content) is list:
                result = f'<{self.tag}>{self.__make_content}</{self.tag}>'
            elif self.content:
                result = f'<{self.tag}>\n  {self.content}\n</{self.tag}>'
            else:
                result = f'<{self.tag}></{self.tag}>' 

        

        elif self.tag_type == 'simple':
            if self.attr != {}:
                result = f'<{self.tag}>' 
            result = f'<{self.tag}>' 
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
        if len(self.content) == 0:
            return ''
        result = '\n'
        space = ''
        for elem in self.content:
            space += '  '
            if isinstance(elem, Elem): 
                print(elem)
                elem = f'{elem}\n'
            result += f'{space}{elem}\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
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
    print(Elem(content=[Text('foo'), Text('bar'), Elem()]))
