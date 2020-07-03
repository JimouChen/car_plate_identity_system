from tkinter import *

# 放置识别得到的车牌结果集
list_plate_word = ''
str_res = str(list_plate_word)


def callback():
    var.set(str_res + e1.get())
    print(str_res)
    print(e1.get())


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

var = StringVar()
var.set('识别结果处')
#
# text_label = Label(root, textvariable=var, justify=LEFT)  # justify设置对齐
# text_label.pack(side=LEFT)  # 排放位置

img = PhotoImage(file='D:/bg_GUI.png')
# img_label = Label(frame1, image=img)
# img_label.pack(side=RIGHT)

Label(frame1, image=img).grid(row=1, column=1, sticky=W, padx=50, pady=30)
Label(frame3, textvariable=var).grid(row=3, column=1, sticky=W, padx=5, pady=5)

Label(frame1, text='图片编号：').grid(row=0, column=0)
e1 = Entry(frame1)
e1.grid(row=0, column=1, padx=10, pady=5)
# img_path = e1.get()


Button(frame2, text='点击启动', command=callback).grid(row=2, column=0, sticky=E, padx=50, pady=50)
Button(frame2, text='开始识别', width=10, command=root.quit).grid(row=2, column=1, sticky=W, padx=50, pady=50)

frame1.pack(padx=100, pady=50)
frame2.pack(padx=100, pady=50)
frame3.pack(padx=10, pady=10)

mainloop()
# 大不了两个gui，前后各一个
