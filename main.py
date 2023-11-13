todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}. {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            todo = input("Enter new todo: ")
            todos[number - 1] = todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("You entered an unknown command")

print("Bye!")