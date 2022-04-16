import PySimpleGUI as sg

def change_theme(theme):
    sg.theme(theme)
    sg.set_options(font = 'Arial 18')
    btn_size = (6,3)
    layout = [
        [sg.Text(
            'output',
            font = 'Arial 21', 
            justification= "center", 
            expand_x= True, 
            pad = (15, 30),
            right_click_menu= theme_menu)
        ],
        [sg.Button('Clear', expand_x= True),sg.Button('Enter', expand_x= True)],
        [sg.Button(7, size = btn_size),sg.Button(8, size = btn_size),sg.Button(9, size = btn_size),sg.Button('*', size = btn_size)],
        [sg.Button(4, size = btn_size),sg.Button(5, size = btn_size),sg.Button(6, size = btn_size),sg.Button('/', size = btn_size)],
        [sg.Button(1, size = btn_size),sg.Button(2, size = btn_size),sg.Button(3, size = btn_size),sg.Button('-', size = btn_size)],
        [sg.Button(0, expand_x= True),sg.Button('.', size = btn_size),sg.Button('+', size = btn_size)],
    ]
    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['Dark', 'DarkGray8','LightGreen3','random']]
window = change_theme('DarkGray8')

current_num = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window = change_theme(event)
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        print(event)
    if event in ['+','-','/','*']:
        print(event)
    if event == 'Enter':
        print(event)
    if event == 'Clear':
        print(event)
window.close()