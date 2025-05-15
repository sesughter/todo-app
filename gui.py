import functions
import PySimpleGUI as sg

label = sg.Text("Enter a todo")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("my-to-do-app",
                   layout=[[label], [input_box, add_button]],
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
        case sg.WINDOW_CLOSED:
            break

window.close()
