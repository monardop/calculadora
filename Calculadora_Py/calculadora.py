import PySimpleGUI as sg

sg.theme('Dark')
sg.set_options(font = 'Arial 18')
btn_size = (6,3)
layout = [
    [sg.Text('output', font = 'Arial 21')],
    [sg.Button('Clear', expand_x= True),sg.Button('Enter', expand_x= True)],
    [sg.Button(7, size = btn_size),sg.Button(8, size = btn_size),sg.Button(9, size = btn_size),sg.Button('*', size = btn_size)],
    [sg.Button(4, size = btn_size),sg.Button(5, size = btn_size),sg.Button(6, size = btn_size),sg.Button('/', size = btn_size)],
    [sg.Button(1, size = btn_size),sg.Button(2, size = btn_size),sg.Button(3, size = btn_size),sg.Button('-', size = btn_size)],
    [sg.Button(0, expand_x= True),sg.Button('.', size = btn_size),sg.Button('+', size = btn_size)],
]
window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()