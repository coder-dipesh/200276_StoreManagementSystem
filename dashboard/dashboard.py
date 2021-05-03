from tkinter import *
from PIL import ImageTk, Image
import time

root = Tk()
root.geometry('1920x1080')
root.title('Store Management System - Dashboard')
root['background'] = '#8e8b8b'

# Creating root Frame for all sub frames
frame = Frame(root)
frame.grid(row=0, column=0, sticky='nsew')

# Creating Header Frame for Title stuff
header = LabelFrame(frame, height=100, width=1920)
header.grid(row=0, column=0)

logo = ImageTk.PhotoImage(Image.open("C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/g.png"))
logo_icon = Label(header, image=logo)
logo_icon.grid(row=0, column=0, padx=5, pady=5)

title = Label(header, text="Store Management System", font=('firacode', 21))
title.grid(row=0, column=1, padx=450)

show_time = Label(header, text="3: 24 : PM",font=('digital-7', 21))
show_time.grid(row=0, column=2,padx=50)


# Creating Menu Frame for sub Button
menu = LabelFrame(frame,pady=30, padx=20)
menu.grid(row=1,column=0,sticky= NW,columnspan=3)

stock_in = Button(menu,padx=70,pady=50,text='Stock In')
stock_in.grid(row=0,column=0,padx=70,pady=50)

sales = Button(menu,padx=75,pady=50, text='Sales',relief=RAISED)
sales.grid(row=1,column=0,padx=70,pady=50)

total = Button(menu,padx=75,pady=50, text='Total')
total.grid(row=2,column=0,padx=70,pady=50)































# clockFrame = Frame(root, width=100, height=50, bd=4, relief="ridge")
# clockFrame.pack(side=RIGHT)
# clockLabel = Label(clockFrame, font=('arial', 12, 'bold'), bd=5, anchor=E)
# clockLabel.pack()
#
# Bottom = Frame(root, width=1350, height=50, bd=4, relief="ridge")
# Bottom.pack(side=BOTTOM, fill=X, expand=1, anchor=S)
#
# def tick(curtime=''):  #acts as a clock, changing the label when the time goes up
#     newtime = time.strftime('%H:%M:%S')
#     if newtime != curtime:
#         curtime = newtime
#         clockLabel.config(text=curtime)
#     clockLabel.after(200, tick, curtime)
#
# tick()  #start clock






# calculator = LabelFrame(root,text="hello world good things takes time",pady=30, padx=20)
# calculator.grid(row=1,column=0,columnspan=3)
#
# btn = Button(root,padx=50,pady=50,text='Helloworld')
# btn.grid(row=0,column=0,padx=10)
#


#
# header = LabelFrame(frame, bg="#8e8b8b", relief="ridge", width=1900, height=100)
# header.grid(row=1, column=0, padx=0, pady=0)
#
# store_logo = ImageTk.PhotoImage(Image.open("F:\PycharmProject\StoremanagementSystem\images\g.png"))
# placing_logo = Label(header, image=store_logo)
# placing_logo.grid(row=0,column=0, padx=5, pady=5)
# # place(x=10, y=10, width=128, height=128)
#
# title = Label(header, text="Store Management System", font=('firacode', 22) )
# title.grid(row=0,column=1,columnspan=3,padx=5, pady=5)
# # place(x=615, y=50)
#
# show_time = Label(header, text='2: 35: PM', font=('firacode', 22))
# show_time.grid(row=0,column=2,padx=5, pady=5)
root.mainloop()
