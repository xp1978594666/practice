import tkinter

baseFrame = tkinter.Tk()

t = tkinter.Text(baseFrame, width=50, height=10)
t.pack()
t.insert(1.4, "I love python")
print(t.get(1.5, 1.8))

# mark_set创建一个标签，可以用来表示位置
t.mark_set("one", 1.6)
t.insert("one", "哈哈")

baseFrame.mainloop()