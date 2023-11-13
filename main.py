while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ") + "\n"

            # opens existing data from file to preserve
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            # append new items
            todos.append(todo)

            # overwrites with a new file the list data
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show" | "display":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}. {item}")
        case "edit":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input("Number of the todo to edit: "))
            todo = input("Enter new todo: ") + "\n"
            todos[number - 1] = todo

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "complete":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "exit":
            break
        case _:
            print("You entered an unknown command")

print("Bye!")