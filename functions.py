def get_todo(filepath = "todos.txt"):
    """Read a text file and return the list of it"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print("hello")