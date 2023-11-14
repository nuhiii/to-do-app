import functions
import PySimpleGUI

# create an instance of a window type
window = PySimpleGUI.Window("My To-Do App", layout=[""])  # title of the window

# display the window on the screen - like print func
window.read()

# close the window instance
window.close()