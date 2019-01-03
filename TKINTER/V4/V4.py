import tkinter
import tkinter.colorchooser as cc

baseFrame = tkinter.Tk()

def cb():
    color  = cc.askcolor("RED", title="选个色子：")
    print(color)
    color  = cc.askcolor("RED", title="Choose Again：")
    print(color)

btn = tkinter.Button(baseFrame, text="open", command=cb)
btn.pack()



baseFrame.mainloop()