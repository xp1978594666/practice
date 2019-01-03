import tkinter

def showLabel():
    global baseFrame
    lb = tkinter.Label(baseFrame, text="显示Label")
    lb.pack()


baseFrame = tkinter.Tk()

btn = tkinter.Button(baseFrame, text="Show Label", command=showLabel)
btn.pack()

baseFrame.mainloop()
