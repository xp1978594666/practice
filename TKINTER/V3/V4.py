import tkinter

baseFrame = tkinter.Tk()

m = tkinter.Menu(baseFrame)
m2 = tkinter.Menu(m)
for item in ['Python', 'Perl', 'Php', 'Rubby']:
    m2.add_checkbutton(label=item)

m2.add_separator()

for item in ['Java', 'C++', 'C']:
    m2.add_radiobutton(label=item)

m.add_cascade(label='Lang', menu=m2)

baseFrame['menu']=m
baseFrame.mainloop()


