def my_var():
    int_ = 42
    str_ = '42'
    string_ = 'quarante-deux'
    float_ = 42.0
    bol = True
    lista = [42]
    dici = {42: 42}
    tupla = (42,)
    set_ = set()

    print(f'{int_} has a type {type(int_)}')
    print(f"{str_} has a type {type(str_)}")
    print(f"{string_} has a type {type(string_)}")
    print(f"{float_} has a type {type(float_)}")
    print(f"{bol} has a type {type(bol)}")
    print(f"{lista} has a type {type(lista)}")
    print(f"{dici} has a type {type(dici)}")
    print(f"{tupla} has a type {type(tupla)}")
    print(f"set() has a type {type(set_)}")


if __name__ == '__main__':
    my_var()