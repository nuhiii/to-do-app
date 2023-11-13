def get_todos(filepath="todos.txt"):
    """
    Read a text file and return the list of
    to-do items.
    """
    # opens existing data from file to preserve
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """
    Write the to-do items list in the text file.
    """
    # overwrites with a new file the list data
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)