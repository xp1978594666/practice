import tkinter

def reg():
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "111" and pwd == "222":
        lb3["text"] = "登录成功"
    else:
        lb3['text'] = "用户名或密码错误"
        e1.delete(0,t1)
        e2.delete(0,t2)

baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, stick=tkinter.W )

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, stick=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码: ")
lb2.grid(row=1, column=0, stick=tkinter.W )

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, stick=tkinter.E)
e2['show'] = '*'

btn = tkinter.Button(baseFrame, text="登录", command = reg)
btn.grid(row=2, column=1, stick=tkinter.E)

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row = 3)




baseFrame.mainloop()

