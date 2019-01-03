import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

emenu = tkinter.Menu(menubar)
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='About')

baseFrame['menu'] = menubar

baseFrame.mainloop()