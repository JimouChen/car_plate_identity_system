"""
# @Time    :  2020/7/3
# @Author  :  Jimou Chen
"""
from tkinter import *



# root = Tk()
#
# frame1 = Frame(root)
# frame2 = Frame(root)
# frame3 = Frame(root)
#
# var = StringVar()
# var.set(str_res)
#
# img = PhotoImage(file='./car_plate.png')
#
# Label(frame1, image=img).grid(row=1, column=1, sticky=W, padx=50, pady=30)
# Label(frame3, textvariable=var).grid(row=2, column=1, sticky=E, padx=50, pady=50)
#
# #
# # Button(frame2, text='点击启动', command=callback2).grid(row=2, column=0, sticky=E, padx=50, pady=50)
# Button(frame2, text='退出系统', width=10, command=root.quit).grid(row=2, column=1, sticky=W, padx=50, pady=50)
#
# frame1.pack(padx=100, pady=50)
# frame2.pack(padx=50, pady=50)
# frame3.pack(padx=10, pady=10)
#
# mainloop()

#
# def show_result(str_res):
#     root = Tk()
#
#     frame1 = Frame(root)
#     frame2 = Frame(root)
#     frame3 = Frame(root)
#
#     var = StringVar()
#     var.set(str_res)
#
#     img = PhotoImage(file='./car_plate.png')
#
#     Label(frame1, image=img).grid(row=1, column=1, sticky=W, padx=50, pady=30)
#     Label(frame3, textvariable=var).grid(row=2, column=1, sticky=E, padx=50, pady=50)
#
#     #
#     # Button(frame2, text='点击启动', command=callback2).grid(row=2, column=0, sticky=E, padx=50, pady=50)
#     Button(frame2, text='退出系统', width=10, command=root.quit).grid(row=2, column=1, sticky=W, padx=50, pady=50)
#
#     frame1.pack(padx=100, pady=50)
#     frame2.pack(padx=50, pady=50)
#     frame3.pack(padx=10, pady=10)
#
#     mainloop()
#
#
# show_result(str_identify)
from identity.tool_function import show_result

str_identify = '21321ued09ud09ud0d030eedy  yd eyd9e yf09y'
show_result(str_identify)
