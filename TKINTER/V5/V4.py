import tkinter

baseFrame = tkinter.Tk()

cvs = tkinter.Canvas(baseFrame, width=300, height=200)
cvs.pack()

cvs.create_line(23,23, 190,234)
cvs.create_text(56,67, text="I LOVE PYTHON")


baseFrame.mainloop()