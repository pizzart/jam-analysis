import PySimpleGUI as sg


def gui_main():
    sg.theme('DarkAmber')
    layout = [
        # [],
        [sg.Text('LD user\'s name/link'), sg.InputText(key='username')],
        [sg.HorizontalSeparator()],
        # [],
        [sg.Text('Graph scale'), sg.Slider(orientation='h',
                                           range=(0.1, 5.0), resolution=0.05, default_value=1, key='scale')],
        [sg.Button('OK')],
    ]

    window = sg.Window(
        'Jam Analysis',
        layout,
        margins=(10, 10),
        finalize=True,
        element_justification='left',
    )

    window['username'].bind("<Return>", "_Enter")

    values = []
    while True:
        event, vals = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return
        elif event == 'OK' or event == 'username' + '_Enter':
            values = vals
            break

    window.close()

    # print(values)
    return values
