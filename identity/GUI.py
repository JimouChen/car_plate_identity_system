from tkinter import *

root = Tk()
root.title('车牌识别系统')

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

var = StringVar()
var.set('欢迎进入车牌识别系统')
img = PhotoImage(file='D:/bg_GUI.png')
# img_label = Label(frame1, image=img)
# img_label.pack(side=RIGHT)

Label(frame1, image=img).grid(row=1, column=1, sticky=W, padx=50, pady=30)
Label(frame3, textvariable=var).grid(row=3, column=1, sticky=W, padx=5, pady=5)
Label(frame1, text='请输入图片编号：').grid(row=0, column=0)

e1 = Entry(frame1)
e1.grid(row=0, column=1, padx=10, pady=5)
Button(frame2, text='开始识别', width=10, command=root.quit).grid(row=2, column=1, sticky=W, padx=50, pady=50)

frame1.pack(padx=100, pady=50)
frame2.pack(padx=100, pady=50)
frame3.pack(padx=10, pady=10)

mainloop()
