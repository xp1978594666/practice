import tkinter
import tkinter.messagebox as mb


baseFrame = tkinter.Tk()



def showError(event):
    msgRst = mb.showerror(title='错误框', message="粗错了")
    print(msgRst)

    msgRst  = mb.askquestion(title="QUESTION", message="May I ask u a question?", icon=mb.INFO)
    print(msgRst)



baseFrame.bind('<Button-1>', showError)


baseFrame.mainloop()

