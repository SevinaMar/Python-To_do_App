import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-do App",layout=[[label], [input_box, add_button]])#each row haw to be a list!!! and has to be a widget
window.read()
window.close()