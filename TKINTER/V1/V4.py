# V4
import tkinter

'''
使用ｂｉｎｄ函数是，函数必须有一个参数，表示ｅｖｅｎｔ
'''

def showLabel(event):
    global baseFrame
    lb = tkinter.Label(baseFrame, text="显示Label")
    lb.pack()


baseFrame = tkinter.Tk()

btn = tkinter.Button(baseFrame, text="Show Label")

btn.bind("<Button-1>", showLabel)
btn.pack()

baseFrame.mainloop()
