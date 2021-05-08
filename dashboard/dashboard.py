# Importing necessary module
from tkinter import *
from PIL import ImageTk, Image
import time
from datetime import datetime

# Defining window
root = Tk()
root.geometry('1920x1080')
root.title('Store Management System - Dashboard')
root['background'] = '#304562'
root.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')

# Creating root Frame for all sub frames
frame = Frame(root,bg='#304562',)
frame.grid(row=0, column=0, sticky='nsew')


# Creating Header Frame for Title stuff
header = LabelFrame(frame, height=100, width=1920,bg='#304562',)
header.grid(row=0, column=0)

# Using logo
logo = ImageTk.PhotoImage(Image.open("C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store-white.png"))
logo_icon = Label(header,bg='#304562',fg='#f7f7f7',image=logo)
logo_icon.grid(row=0, column=0, padx=5,ipadx=25, pady=5)

# Heading Title
title = Label(header, bg='#304562',fg='#f7f7f7',text="Store Management System",font=('HandVetica',37))
title.grid(row=0, column=1, padx=350)

# Creating clock
def clock():
    hour= time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    unit = time.strftime('%p')

    show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
    show_time.after(1000,clock)

#Displaying time
show_time = Label(header,bg='#304562',fg='#fbfbfb', text="",font=('digital-7', 22))
show_time.grid(row=0, column=2,padx=30)


clock()

# Creating Menu Frame for sub Button
menu = LabelFrame(frame,pady=23, padx=80,bg='#091b33',borderwidth=0)
menu.grid(row=1,column=0,sticky= NW,)

# Buttons for sub page
stock_in = Button(menu,padx=50,pady=30,text='Stock In',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",)
stock_in.grid(row=0,column=0,padx=60,pady=17,ipady=15)

sales = Button(menu,padx=72,pady=30, text='Sales',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",)
sales.grid(row=1,column=0,padx=50,ipady=15,pady=15)

update = Button(menu,padx=63,pady=30, text='Update',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",)
update.grid(row=2,column=0,padx=50,ipady=15,pady=15)

total = Button(menu,padx=70,pady=30, text='Total',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",)
total.grid(row=3,column=0,padx=52,ipady=15,pady=17)

# Creating frame for date and logout section

sub_header = LabelFrame(frame,bg='#304562',borderwidth=0)
sub_header.grid(row=1,column=0,columnspan=3,sticky=NE,ipady=10,)

def date():
    year = time.strftime('%Y')
    month = time.strftime('%b')
    day = time.strftime('%d')

    date_sec.config(text=year + ' ' + month + ' ' + day )
    date_sec.after(1000, date)

# For displaying date
date_sec = Label(sub_header, fg='#f7f7f7', bg='#304562', text='', font=('digital-7',21))
date_sec.grid(row=0, column=0,ipady=10,sticky=NW,padx=318)

date()


# Button with icon for logout
icon_logout = ImageTk.PhotoImage(Image.open('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/logout-white.png'))
logout = Button(sub_header, bg='#304562',image=icon_logout,relief=FLAT)
logout.grid(row=0,column=3,padx=100,ipady=12,)

# Creating frame for calculator section

# Creating main frame for calculator
calcFrame = LabelFrame(frame,bg='#091b33',borderwidth=0,padx=27,pady=15)
calcFrame.grid(row=1, column=0,sticky=NE,padx=210,pady=200)

# Creating input field
inputField = Entry(calcFrame, width=72, bg="#fbfbfb")
inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10,ipadx=80, ipady=17)


# # Creating numeric buttons
button_0 = Button(calcFrame, text="0", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_1 = Button(calcFrame, text="1", padx=43, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_2 = Button(calcFrame, text="2", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_3 = Button(calcFrame, text="3", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_4 = Button(calcFrame, text="4", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_5 = Button(calcFrame, text="5", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_6 = Button(calcFrame, text="6", padx=45, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_7 = Button(calcFrame, text="7", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_8 = Button(calcFrame, text="8", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )
button_9 = Button(calcFrame, text="9", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15), )

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
button_add = Button(calcFrame, text="➕", padx=32, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,), )
button_sub = Button(calcFrame, text="−", padx=41, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,), )
button_mul = Button(calcFrame, text="x", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,), )
button_div = Button(calcFrame, text="÷", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,), )
button_equal = Button(calcFrame, text="=", padx=163, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,), )

# Putting calculation buttons on screen
button_add.grid(row=1, column=1, padx=5, pady=5)
button_sub.grid(row=1, column=2, padx=5, pady=5)
button_mul.grid(row=4, column=0, padx=0, pady=5)
button_div.grid(row=4, column=1, padx=9, pady=5)
button_equal.grid(row=4, column=2, columnspan=3, padx=5, pady=5)

# Creating special buttons
button_clear = Button(calcFrame, text="C", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15, "bold"), )
button_off = Button(calcFrame, text="Off", padx=90, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,), )

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

# tick()  #start clock

# calculator = LabelFrame(root,text="hello world good things takes time",pady=30, padx=20)
# calculator.grid(row=1,column=0,columnspan=3)
#
# btn = Button(root,padx=50,pady=50,text='Helloworld')
# btn.grid(row=0,column=0,padx=10)
root.mainloop()
