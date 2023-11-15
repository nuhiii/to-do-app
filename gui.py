import functions
import PySimpleGUI

# create a text type of the gui instance to create a label on the window
label = PySimpleGUI.Text("Type in a to-do")
# text input
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
# button widget
add_button = PySimpleGUI.Button("Add")
# read the todos from file function and export them to a list box for display on window
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key="todos",
                               enable_events=True, size=[45, 10])
# edit button next to to do list box item
edit_button = PySimpleGUI.Button("Edit")
# complete button after edit to mark off tasks
complete_button = PySimpleGUI.Button("Complete")
# exit button to quit program
exit_button = PySimpleGUI.Button("Exit")

# create an instance of a window type
window = PySimpleGUI.Window("My To-Do App",  # title of the window
                            layout=[[label], [input_box, add_button],
                                    # each row [] of widgets displayed
                                    [list_box, edit_button, complete_button], [exit_button]],
                            font=("Helvetica", 20))

# keep the window open
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            # get the edit values
            todo_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            # update on the text file
            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            # update on the gui
            window["todos"].update(values=todos)
        case "Complete":
            todo_complete = values["todo"][0]
            todos = functions.get_todos()
            todos.remove(todo_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            # select item from list box and have it appear on the text field
            window["todo"].update(value=values["todos"][0])
        # close the window gui program when red x button is clicked
        case PySimpleGUI.WIN_CLOSED:
            break

# close the window instance
window.close()
