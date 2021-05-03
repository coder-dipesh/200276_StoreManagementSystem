from tkinter import *
from PIL import ImageTk, Image
root =  Tk()
root.title('Store Management System - Stock In')
root.geometry('1920x1080')


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

# Creating Product Details Section

frameRight = LabelFrame(frame, height=600, width=800)
frameRight.grid(row=1, column=0, padx=20, pady=40, sticky='nw')

title = Label(frameRight, text="Product Details")
title.grid(row=0,column=1, padx=80)

id = Label(frameRight, text='Bill No')
id.grid(row=1,column=0, sticky='nw')

id_entry = Entry(frameRight)
id_entry.grid(row=1, column=2,padx=10)

product_name = Label(frameRight, text='Product Name')
product_name.grid(row=2,column=0,pady=10,sticky='nw')

pname_entry = Entry(frameRight)
pname_entry.grid(row=2, column=2)

vendor = Label(frameRight, text='Product Quantity')
vendor.grid(row=3,column=0)

vendor_name= Entry(frameRight)
vendor_name.grid(row=3, column=2,padx=10)

price = Label(frameRight, text='Product Rate')
price.grid(row=4,column=0,pady=10,sticky='nw')

price_ = Entry(frameRight)
price_.grid(row=4, column=2,padx=10,)

total_price = Label(frameRight, text='Total Price')
total_price.grid(row=5,column=0,sticky='nw')

total_price_entry = Entry(frameRight)
total_price_entry.grid(row=5, column=2,pady=10,padx=10,)

# Creating Vendor Details Section


frameRight = LabelFrame(frame,height=300, width=400)
frameRight.grid(row=1,column=0,padx=50,pady=40,sticky='ne' )

title = Label(frameRight, text="Vendor Details")
title.grid(row=0,column=1,padx=80)


id = Label(frameRight, text='Company Name')
id.grid(row=1,column=0,pady=10,sticky='nw')

id_entry = Entry(frameRight)
id_entry.grid(row=1, column=2,padx=10)

product_name = Label(frameRight, text='Address')
product_name.grid(row=2,column=0,sticky='nw',)

pname_entry = Entry(frameRight)
pname_entry.grid(row=2, column=2)

vendor = Label(frameRight, text='Contact')
vendor.grid(row=3,column=0,pady=10,sticky='nw')

vendor_name= Entry(frameRight)
vendor_name.grid(row=3, column=2,padx=10)

price = Label(frameRight, text='Email')
price.grid(row=4,column=0,sticky='nw')

price_ = Entry(frameRight)
price_.grid(row=4, column=2,padx=10,pady=10)

# Creating Footer frame

footer = LabelFrame(frame,width=400)
footer.grid(row=2,column=0,padx=20,sticky='nw')

description_label = Label(footer,text= "Product Description")
description_label.grid(row=0,column=0,sticky="nw")

description= Text(footer,height=10,width=54,font=('firacode',12))
description.grid(row=1,column=0,sticky='nw')

# Creating Add stock section frame

add_stock_frame = LabelFrame(frame,)
add_stock_frame.grid(row=2,column=0,padx=350,pady=40,sticky='e')


add_stock = Button(add_stock_frame,padx=60, pady=30,text="Add Stock")
add_stock.grid(row=0,column=0,)





mainloop()