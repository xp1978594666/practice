import tkinter

def makeLabel():
    global baseFrame
    tkinter.Label(baseFrame, text="PHP是最好的编程语言，我用Python").pack()

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)
for x in ['麻辣香菇', '气锅鸡', '东坡肘子']:
    menubar.add_separator()
    menubar.add_command(label=x)
menubar.add_command(label='重庆火锅', command=makeLabel)


def pop(event):
    # 注意使用 event.x 和 event.x_root的区别
    #menubar.post(event.x_root, event.y_root)
    menubar.post(event.x_root, event.y_root)

baseFrame.bind("<Button-3>", pop)

