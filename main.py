def get_todos():
    # opens existing data from file to preserve
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type 'add', 'edit', or 'complete' followed by the todo action, "
                        "or type 'show' to display list or 'exit' to quit program: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        # append new items
        todos.append(todo)

        # overwrites with a new file the list data
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            todos[number - 1] = input("Enter new todo: ") + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            completed = todos.pop(number - 1).strip("\n")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f'The to do item "{completed}" was removed from the list.')
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered an unknown command")

print("Bye!")