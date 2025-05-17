import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("black")
clock_label = sg.Text('', key="Clock")
label = sg.Text("Enter a todo")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todo(),
                      key="todos", enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit")

window = sg.Window("my-to-do-app",
                   layout=[[clock_label], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read(timeout=200)
    window["Clock"].update(value=time.strftime("%m - %b - %Y - %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window["todos"].update(todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"] + "\n"
                todo = functions.get_todo()
                index = todo.index(todo_to_edit)
                todo[index] = new_todo
                functions.write_todo(todo)
                window["todos"].update(values=todo)
            except IndexError:
                sg.popup("please select an item first", font=("Helvetica", 20))
        case "complete":
            try:
                todo_to_complete = value["todos"][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select an item first", font=("Helvetica", 20))
        case "todos":
            window['todo'].update(value=value["todos"][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
