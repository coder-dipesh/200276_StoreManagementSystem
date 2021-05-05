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
menu = LabelFrame(frame,pady=20, padx=80)
menu.grid(row=1,column=0,sticky= NW,)

stock_in = Button(menu,padx=70,pady=50,text='Stock In')
stock_in.grid(row=0,column=0,padx=70,pady=30)

sales = Button(menu,padx=75,pady=50, text='Sales',)
sales.grid(row=1,column=0,padx=70,pady=30)

update = Button(menu,padx=75,pady=50, text='Update',)
update.grid(row=2,column=0,padx=70,pady=30)

total = Button(menu,padx=78,pady=50, text='Total')
total.grid(row=3,column=0,padx=70,pady=30)

# Creating frame for date and logout section
# height=200

sub_header = LabelFrame(frame,)
sub_header.grid(row=1,column=0,columnspan=3,sticky=NE,ipady=10)

date_sec = Label(sub_header, text='2078/7/4',font=('digital-7',21))
date_sec.grid(row=0, column=0,ipady=10,sticky=NW,padx=332)

icon_logout = ImageTk.PhotoImage(Image.open('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/logout.png'))

logout = Button(sub_header, image=icon_logout,relief=FLAT)
logout.grid(row=0,column=3,padx=100,ipady=10,)

# Creating frame for calculator section

# Creating Frame
calcFrame = LabelFrame(frame)
calcFrame.grid(row=1, column=0,sticky=NE,padx=210,pady=200)

# Creating input field
inputField = Entry(calcFrame, width=70, bg="#f0ece2")
inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10,ipadx=70, ipady=15)


# # Creating numeric buttons
button_0 = Button(calcFrame, text="0", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_1 = Button(calcFrame, text="1", padx=43, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_2 = Button(calcFrame, text="2", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_3 = Button(calcFrame, text="3", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_4 = Button(calcFrame, text="4", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_5 = Button(calcFrame, text="5", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_6 = Button(calcFrame, text="6", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_7 = Button(calcFrame, text="7", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_8 = Button(calcFrame, text="8", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )
button_9 = Button(calcFrame, text="9", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15), )

# Putting buttons on screen
button_0.grid(row=2, column=0, padx=5, pady=5)
button_1.grid(row=3, column=4, padx=5, pady=5)
button_2.grid(row=3, column=3, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_4.grid(row=3, column=1, padx=5, pady=5)
button_5.grid(row=3, column=0, padx=5, pady=5)
button_6.grid(row=2, column=4, padx=5, pady=5)
button_7.grid(row=2, column=3, padx=5, pady=5)
button_8.grid(row=2, column=2, padx=5, pady=5)
button_9.grid(row=2, column=1, padx=5, pady=5)

# Creating calculation buttons
button_add = Button(calcFrame, text="➕", padx=38, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), )
button_sub = Button(calcFrame, text="−", padx=37, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), )
button_mul = Button(calcFrame, text="x", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), )
button_div = Button(calcFrame, text="÷", padx=38, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), )
button_equal = Button(calcFrame, text="=", padx=156, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), )

# Putting calculation buttons on screen
button_add.grid(row=1, column=1, padx=5, pady=5)
button_sub.grid(row=1, column=2, padx=5, pady=5)
button_mul.grid(row=4, column=0, padx=0, pady=5)
button_div.grid(row=4, column=1, padx=5, pady=5)
button_equal.grid(row=4, column=2, columnspan=3, padx=5, pady=5)

# Creating special buttons
button_clear = Button(calcFrame, text="C", padx=40, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15, "bold"), )
button_off = Button(calcFrame, text="Off", padx=90, pady=20, bg="#525252", fg="#f0ece2", font=('digital-7', 15,), )

# Putting special buttons on screen
button_clear.grid(row=1, column=0, padx=5, pady=5)
button_off.grid(row=1, column=3, columnspan=2, padx=5, pady=5)


























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
