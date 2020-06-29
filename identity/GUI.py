from tkinter import *


def callback():
    var.set('hhh')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('helllo')

text_label = Label(frame1, textvariable=var, justify=LEFT)
text_label.pack(side=LEFT)

img = PhotoImage(file='D:/1.jpg')
img_label = Label(frame1, image=img)
img_label.pack(side=RIGHT)

the_button = Button(frame2, text='222', command=callback)
the_button.pack()

frame1.pack(padx=100, pady=100)
frame2.pack(padx=100, pady=100)


mainloop()
