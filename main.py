while True:
    user_action = input("Type 'add', 'edit', or 'complete' followed by the todo action, "
                        "or type 'show' to display list or 'exit' to quit program: ").strip()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        # opens existing data from file to preserve
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # append new items
        todos.append(todo)

        # overwrites with a new file the list data
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # # list comprehension to remove the extra \n line that print generates on top of existing \n on list
        # # when printing to console
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif "edit" in user_action:
        number = int(user_action[5:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos[number - 1] = input("Enter new todo: ") + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        completed = todos.pop(number - 1).strip("\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        print(f'The to do item "{completed}" was removed from the list.')

    elif "exit" in user_action:
        break

    else:
        print("You entered an unknown command")

print("Bye!")