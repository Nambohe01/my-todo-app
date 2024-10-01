FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """This is for reading the text file and returning the list of todos"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def store_todos(todos_arg, filepath=FILEPATH):
    """This is for writing the new to the list"""
    # Get Current todos

    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Adios")
    print(get_todos())
