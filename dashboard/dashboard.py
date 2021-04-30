from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('1920x1080')
root.title('Store Management System - Dashboard')
root['background']='#8e8b8b'

frame = Frame(root)
frame.grid(row=0,column=0)

header = LabelFrame(frame,height=100, width=1900)
header.grid(row=0,column=0)

logo = ImageTk.PhotoImage(Image.open("F:\PycharmProject\StoremanagementSystem\images\g.png"))
logo_icon = Label(header, image=logo)
logo_icon.grid(row=0,column=0, padx=5,pady=5)

title = Label(header, text="Store Management System",font=('firacode', 21))
title.grid(row=0,column=1,padx=400)

show_time = Label(header, text="3: 24 : PM",font=('firacode', 21))
show_time.grid(row=0,column=2,padx=150)












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
