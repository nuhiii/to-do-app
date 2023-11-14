import functions
import PySimpleGUI

# create a text type of the gui instance to create a label on the window
label = PySimpleGUI.Text("Type in a to-do")
# text input
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
# button widget
add_button = PySimpleGUI.Button("Add")

# create an instance of a window type
window = PySimpleGUI.Window("My To-Do App",  # title of the window
                            layout=[[label], [input_box, add_button]],  # each row [] of widgets displayed
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
        # close the window gui program when red x button is clicked
        case PySimpleGUI.WIN_CLOSED:
            break


# close the window instance
window.close()