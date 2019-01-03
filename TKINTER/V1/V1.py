import tkinter


base = tkinter.Tk()
base.wm_title("Label Test")
# 支持属性很多background, font, underline等
# 第一个参数，制定所属
lb = tkinter.Label(base, text="Python AI")
lb.pack()

base.mainloop()
