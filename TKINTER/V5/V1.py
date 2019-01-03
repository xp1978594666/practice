import tkinter


baseFrame = tkinter.Tk()

time1 = 0
time2 = 0

def textPython():
    global lb, cbPython, time1

    if time1 % 2 == 0:
        time1 += 1
        lb['text'] = "Python被选择"
    else:
        time1 += 1
        lb['text'] = "Python被取消"


''''
IntVar，StringVar此类数据的使用需要在 tkinter.Tk()之后，否则报错
'''
v = tkinter.IntVar()

def textJava():
    value = v.get()
    if value == 0:
        lb['text'] = "Java被取消"
    else:
        lb['text'] = "Java被选中"






cbPython = tkinter.Checkbutton(baseFrame, text="Python", command=textPython)
cbPython.pack()

cbJava = tkinter.Checkbutton(baseFrame, variable=v, text="Java", command=textJava)
cbJava.pack()

lb = tkinter.Label(baseFrame, text= "   ")
lb.pack()

baseFrame.mainloop()
