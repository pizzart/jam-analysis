import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# matplotlib.use("TkAgg")


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


def gui_main():
    layout = [
        # [sg.Text("")],
        # [sg.Canvas(key="-CANVAS-", size=(1600, 1200))],
        [sg.InputText(), sg.Button("OK")],
    ]

    window = sg.Window(
        "Jam Analysis",
        layout,
        location=(0, 0),
        finalize=True,
        element_justification="center",
        # size=(2000, 1800)
        # font="Helvetica 18",
    )

    # draw_figure(window["-CANVAS-"].TKCanvas, fig)

    event, values = window.read()

    window.close()
