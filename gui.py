import functions
import PySimpleGUI

# create a text type of the gui instance to create a label on the window
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
add_button = PySimpleGUI.Button("Add")

# create an instance of a window type
window = PySimpleGUI.Window("My To-Do App", layout=[[label], [input_box, add_button]])
# title of the window and each row [] displayed

# display the window on the screen - like print func
window.read()

# close the window instance
window.close()