import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todo(),
                      key="todos", enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("my-to-do-app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window["todos"].update(todos)
        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"] + "\n"
            todo = functions.get_todo()
            index = todo.index(todo_to_edit)
            todo[index] = new_todo
            functions.write_todo(todo)
            window["todos"].update(values=todo)
        case sg.WINDOW_CLOSED:
            break

window.close()
