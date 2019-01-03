import tkinter

baseFrame = tkinter.Tk()

btn1 = tkinter.Button(baseFrame, text="测试按钮")
btn1['width'] = 30
btn1['height'] = 30
btn1.pack()

btn2 = tkinter.Button(baseFrame, text="显示按钮")
btn2['width'] = 20
btn2['height'] = 30
btn2['background'] = 'green'
btn2.pack()

baseFrame.mainloop()