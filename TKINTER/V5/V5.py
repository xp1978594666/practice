import tkinter
import math as m

baseFrame = tkinter.Tk()

w = tkinter.Canvas(baseFrame, width=300, height=300, background="gray" )
w.pack()


center_x = 150
center_y = 150

r = 150

points = [
    #左上点
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),

    #右上点
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),

    #左下点
    center_x - int(r * m.sin( m.pi / 5)),
    center_y + int(r * m.cos( m.pi / 5)),

    #顶点
    center_x,
    center_y - r,

    #右下点
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
]

w.create_polygon(points, outline="green", fill="yellow")
w.create_text(150,150, text="五角星")

baseFrame.mainloop()