import functions
import time

date = time.strftime("%m - %b - %y - %H:%M:%Y")
print(date)

while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todo()

        todos.append(todo)

        functions.write_todo("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = functions.get_todo()

        new_todos = []
        for i in todos:
            items = i.strip("\n")
            new_todos.append(items)
        for i, e in enumerate(new_todos):
            row = f"{i + 1}. {e}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todo()

            number = int(user_action[5:]) - 1
            new_todo = input("enter new todo: ") + "\n"
            todos[number] = new_todo

        except ValueError:
            print("wrong command")
            continue

        functions.write_todo("todos.txt", todos)
    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todo()

            user_pick = int(user_action[9:])
            todos.pop(user_pick - 1)

            functions.write_todo("todos.txt", todos)
        except IndexError:
            print("No todo with that number")
            continue
    elif user_action.startswith("exit"):
        break

    else:
        print("command not valid")

print("Good bye")
