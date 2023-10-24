from path import Path

def using_path():
    path = Path.getcwd() + '/new_directory'
    path.mkdir()
    file = Path(f'{path}/new_file.txt')
    file.write_text('Hello, word!\nMy name is Sandy Nascimento.')
    print(file.read_text())

if __name__ == '__main__':
    using_path()