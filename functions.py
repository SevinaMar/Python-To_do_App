FILE_PATH = (r'todos.txt')
def read_todos(file_path_local = FILE_PATH):
    """ Read a text file and return a list """
    with open(file_path_local, 'r') as file_local:
        text = file_local.readlines()
    return text

def write_todos(text, file_path_local = FILE_PATH ):
    """ Write a to-do list in a text file"""  #DOCSTRINGS
    with open(file_path_local,'w') as file_local:
        file_local.writelines(text)