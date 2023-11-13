while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ") + "\n"

            # opens existing data from file to preserve
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # append new items
            todos.append(todo)

            # overwrites with a new file the list data
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "show" | "display":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # # list comprehension to remove the extra \n line that print generates on top of existing \n on list
            # # when printing to console
            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            todo = input("Enter new todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos[number - 1] = todo

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            completed = todos.pop(number - 1).strip("\n")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f'The to do item "{completed}" was removed from the list.')
        case "exit":
            break
        case _:
            print("You entered an unknown command")

print("Bye!")