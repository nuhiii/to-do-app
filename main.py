todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index}. {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            todo = input("Enter new todo: ")
            todos[number - 1] = todo
        case "exit":
            break
        case _:
            print("You entered an unknown command")

print("Bye!")