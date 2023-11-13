# from functions import get_todos, write_todos
# with the above code we don't have to write functions.method()
# as we are importing the specific functions we will use
# if we had a folder named modules where functions.py existed, then we write:
# from modules import functions
# with the below, we have to use functions.method() but it makes it easier
# to see where our functions are coming from
import functions

while True:
    user_action = input("Type 'add', 'edit', or 'complete' followed by the todo action, "
                        "or type 'show' to display list or 'exit' to quit program: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        # append new items
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            todos[number - 1] = input("Enter new todo: ") + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            completed = todos.pop(number - 1).strip("\n")
            functions.write_todos(todos)
            print(f'The to do item "{completed}" was removed from the list.')
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered an unknown command")

print("Bye!")