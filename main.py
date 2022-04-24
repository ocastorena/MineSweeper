from tkinter import *

# override the window settings
root = Tk()
root.geometry('1080x720')
root.title("MineSweeper")
root.resizable(False, False)
root.configure(bg="black")

# frame
top_frame = Frame(
    root,
    bg="red",
    width=1080,
    height=180
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="blue",
    width=216,
    height=720
)
left_frame.place(x=0, y=180)

# run the window
root.mainloop()
