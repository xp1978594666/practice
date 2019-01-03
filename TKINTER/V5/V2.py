import tkinter


baseFrame = tkinter.Tk()

def textSelect():
    global lb

    value = v.get()
    print(value)

    if value == 0:
        lb['text'] = "Python被选择"
        return None

    if value == 1:
        lb['text'] = "Java被选择"
        return None

    print("ERRRRRRRRRRRROR........{0}".format(value))
    return None


''''
IntVar，StringVar此类数据的使用需要在 tkinter.Tk()之后，否则报错
'''
v = tkinter.IntVar()



cbPython = tkinter.Radiobutton(baseFrame, variable=v, text="Python",  value=0, command=textSelect)
cbPython.pack()

cbJava = tkinter.Radiobutton(baseFrame, variable=v, text="Java", value=1,  command=textSelect)
cbJava.pack()

lb = tkinter.Label(baseFrame, text= "   ")
lb.pack()

baseFrame.mainloop()
