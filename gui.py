# NOT YET USED

import PySimpleGUI as sg
# import matplotlib
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# matplotlib.use("TkAgg")


# def draw_figure(canvas, figure):
#     figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
#     figure_canvas_agg.draw()
#     figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
#     return figure_canvas_agg


def gui_main():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('LD username/link:')],
        # [sg.Canvas(key="-CANVAS-", size=(1600, 1200))],
        [sg.InputText(), sg.Button('OK')],
    ]

    window = sg.Window(
        'Jam Analysis',
        layout,
        # location=(0, 0),
        finalize=True,
        element_justification='left',
        # size=(2000, 1800)
        # font="Helvetica 18",
    )

    # draw_figure(window["-CANVAS-"].TKCanvas, fig)

    values = []
    while True:
        event, vals = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        elif event == 'OK':
            values = vals
            break

    window.close()

    return values
