from tkinter import *
import settings
import utils

# override the window settings
root = Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("MineSweeper")
root.resizable(False, False)
root.configure(bg="black")

# frame
top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_percent(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_percent(20),
    height=settings.HEIGHT
)
left_frame.place(x=0, y=utils.height_percent(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_percent(80),
    height=utils.height_percent(75)
)
center_frame.place(
    x=utils.width_percent(20),
    y=utils.height_percent(25)
)

# run the window
root.mainloop()
