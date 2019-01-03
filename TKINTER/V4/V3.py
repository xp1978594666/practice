import tkinter
import tkinter.filedialog as fd


baseFrame = tkinter.Tk()

def showFD(event):
    fileName = fd.askopenfilename()
    print(fileName)

    # 需要注意次函数返回值是一个结构, 非普通字符串
    fileName = fd.askopenfile()
    print(fileName)

    fileName = fd.askdirectory()
    print(fileName)

    fileName = fd.asksaveasfile()
    print(fileName)

baseFrame.bind('<Button-1>', showFD)

baseFrame.mainloop()
