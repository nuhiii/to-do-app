def get_todos(filepath):
    # opens existing data from file to preserve
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    # overwrites with a new file the list data
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type 'add', 'edit', or 'complete' followed by the todo action, "
                        "or type 'show' to display list or 'exit' to quit program: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos("todos.txt")
        # append new items
        todos.append(todo)
        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos("todos.txt")
            todos[number - 1] = input("Enter new todo: ") + "\n"
            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("todos.txt")
            completed = todos.pop(number - 1).strip("\n")
            write_todos("todos.txt", todos)
            print(f'The to do item "{completed}" was removed from the list.')
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered an unknown command")

print("Bye!")