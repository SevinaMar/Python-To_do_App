import os
import time
from functions import *
#or import function and them functions.read_todos()...



now = time.strftime("%d %B %Y  %H:%M:%S")
print("It is ", now)
"""Adds a date and time"""

"""να προσθέσω δυνατότητα νέας λίστας-->δηλαδή ,έο αρχείο
new list
άαα να δω την ασκηση με τη λίστα τίτλων . μία λίστα λιστών!"""
"""Looking for existing file"""
if not os.path.isfile(FILE_PATH):
    write_todos("")
else:
    todos = read_todos()
print("------------------------------\nThe possible actions are:\n-add (a todo) \n-display (todo list) \n-edit (number of list item) \n-remove (number of list item) \n-or exit")

while True:
    user_action = (input("Choose an action: "))
    user_action = user_action.strip()

    if user_action.startswith("add"):
    #if 'add' in user_action[:4]:
        todo = user_action[4:] + '\n'
        todo = todo.title()
        todos = read_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("display"):
        todos = read_todos()
        if len(todos) == 0:
            print("Your list is empty.")
        else:
            for index, do in enumerate(todos):
                do = do.strip("\n")
                do = do.title()
                print(f"{index + 1} - {do}")

    elif user_action.startswith("edit"):
        try:
            todo_num = int(user_action[5:])
            todo_num -= 1
            todos = read_todos()
            print("--existing list:", todos)
            new_todo = input("You can now enter a new todo: ")
            todos[todo_num] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Please choose one of the approved commands.")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[7:])
            todos = read_todos()
            todos.pop(number - 1)
            write_todos(todos)
        except IndexError:
            print("Wrong index number. Try again, please: ")
            continue

        # for index, do in enumerate(todos):
        #     do = do.title()
        #     print(f"{index + 1}-  {do}")

    elif user_action.startswith('exit'):
        print("-programme ternimating-")
        break
    else:
        print("Please choose one of the approved commands.")