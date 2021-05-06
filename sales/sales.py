from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Store Management System - Sales')
root.geometry('1920x1080')
root.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
root['background'] = '#304562'

# Creating root Frame for all sub frames
frame = Frame(root,bg='#304562',)
frame.grid(row=0, column=0, sticky='nsew')

# Creating Header Frame for Title stuff
header = LabelFrame(frame, height=100, width=1920,bg='#304562')
header.grid(row=0, column=0)

logo = ImageTk.PhotoImage(Image.open("C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store-white.png"))
logo_icon = Label(header, image=logo,bg='#304562')
logo_icon.grid(row=0, column=0, padx=5, pady=5)

title = Label(header, text="Store Management System",bg='#304562',fg='#f7f7f7', font=('HandVetica',37))
title.grid(row=0, column=1, padx=350)

show_time = Label(header, text="3: 24 : PM", font=('digital-7', 21),bg='#304562',fg='#f7f7f7')
show_time.grid(row=0, column=2, padx=50)

# Creating frame to insert back button
back_btn = ImageTk.PhotoImage(Image.open("C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/back-arrow-white.png"))

back_home = Frame(frame,height=40, width=50)
back_home.grid(row=1,column=0,padx=10,pady=10,sticky='nw')

back_home_btn = Button(back_home,bg='#304562',image=back_btn,relief=FLAT, padx=20, pady=20)
back_home_btn.grid(row=0, column=0)


# Creating Product Details Section

productFrame = LabelFrame(frame, height=600, pady=10,padx=10,width=800,bg='#091b33')
productFrame.grid(row=2, column=0, padx=20, pady=40, sticky='nw')

title = Label(productFrame,bg='#091b33',fg='#f7f7f7', text="Product Details", font=('Code New Roman',14))
title.grid(row=0,column=1, padx=70)

billno = Label(productFrame,bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman',14))
billno.grid(row=1,column=0, sticky='nw')

billno_entry = Entry(productFrame)
billno_entry.grid(row=1, column=2,padx=10, ipadx=50, ipady=10)

productName = Label(productFrame,bg='#091b33',fg='#f7f7f7',  text='Product Name', font=('Code New Roman',14))
productName.grid(row=2,column=0,pady=10,sticky='nw')

productName_entry = Entry(productFrame)
productName_entry.grid(row=2, column=2, ipadx=50, ipady=10)

productQuantity = Label(productFrame,bg='#091b33',fg='#f7f7f7',  text='Product Quantity', font=('Code New Roman',14))
productQuantity.grid(row=3,column=0)

productQuantity_entry= Entry(productFrame)
productQuantity_entry.grid(row=3, column=2,padx=10, ipadx=50, ipady=10)

rate = Label(productFrame, bg='#091b33',fg='#f7f7f7', text='Product Rate', font=('Code New Roman',14))
rate.grid(row=4,column=0,pady=10,sticky='nw')

rate_entry = Entry(productFrame)
rate_entry.grid(row=4, column=2,padx=10, ipadx=50, ipady=10)

totalPrice = Label(productFrame,bg='#091b33',fg='#f7f7f7',  text='Total Price', font=('Code New Roman',14))
totalPrice.grid(row=5,column=0,sticky='nw')

totalPrice_entry = Entry(productFrame)
totalPrice_entry.grid(row=5, column=2,padx=10,ipadx=50, ipady=10)

# Creating Vendor Details Section


vendorFrame = LabelFrame(frame, height=600, pady=10,padx=10,width=800,bg='#091b33')
vendorFrame.grid(row=2, column=0, padx=20, pady=40, sticky='ne')

title = Label(vendorFrame,bg='#091b33',fg='#f7f7f7', text="Vendor Details", font=('Code New Roman',14))
title.grid(row=0,column=1, padx=70)

companyName = Label(vendorFrame,bg='#091b33', fg='#f7f7f7', text='Company Name', font=('Code New Roman',14))
companyName.grid(row=1,column=0, sticky='nw')

companyName_entry = Entry(vendorFrame)
companyName_entry.grid(row=1, column=2,padx=10, ipadx=50, ipady=10)

address = Label(vendorFrame,bg='#091b33',fg='#f7f7f7',  text='Address', font=('Code New Roman',14))
address.grid(row=2,column=0,pady=10,sticky='nw')

address_entry = Entry(vendorFrame)
address_entry.grid(row=2, column=2, ipadx=50, ipady=10)

contactNumber = Label(vendorFrame,bg='#091b33',fg='#f7f7f7',  text='Contact Number', font=('Code New Roman',14))
contactNumber.grid(row=3,column=0)

contactNumber_entry= Entry(vendorFrame)
contactNumber_entry.grid(row=3, column=2,padx=10, ipadx=50, ipady=10)

email = Label(vendorFrame, bg='#091b33',fg='#f7f7f7', text='Email', font=('Code New Roman',14))
email.grid(row=4,column=0,pady=10,sticky='nw')

email_entry = Entry(vendorFrame)
email_entry.grid(row=4, column=2,padx=10, ipadx=50, ipady=10)

date = Label(vendorFrame,bg='#091b33',fg='#f7f7f7',  text='Date', font=('Code New Roman',14))
date.grid(row=5,column=0,sticky='nw')

date_entry = Entry(vendorFrame,)
date_entry.grid(row=5, column=2,padx=10,ipadx=50, ipady=10)

# Creating Add stock section frame

add_stock_frame = LabelFrame(frame,bg='#091b33',)
add_stock_frame.grid(row=3,column=0,padx=350,pady=40,)


add_stock = Button(add_stock_frame,borderwidth=0,padx=95,bg='#06e6b0',fg='#091b33', pady=30,text="Sales",font=('Code New Roman',21))
add_stock.grid(row=0,column=0,)





mainloop()