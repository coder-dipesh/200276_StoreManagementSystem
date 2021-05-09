# Importing necessary module
import sqlite3
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox


# -------------------------------------Creating database table --------------------------------------------------------------#

# Creating databases with sub table

# --------------------------------------- Authentication Table ------------------------------------------------------------#
# # Database queries for Authentication
# # Giving database name
# main_database = sqlite3.connect('storemanagement.db')
#
# # Initializing cursor
# c = main_database.cursor()
#
# # Creating authentication table
# c.execute("""CREATE TABLE authentication(
#             first_name text,
#             last_name text,
#             email_address text,
#             username text,
#             password text
# )
# """)
# print('Table created for Authentication.')
#
# # Committing and closing the database.
# main_database.commit()
# main_database.close()

# --------------------------------------- End of authentication table------------------------------------------------------#

# ---------------------------------------  Data storage table -------------------------------------------------------------#
# Database queries for Data storage
# Giving database name
# main_database = sqlite3.connect('storemanagement.db')
#
# # Initializing cursor
# c = main_database.cursor()
#
# # Creating authentication table
# c.execute("""CREATE TABLE data_storage(
#             bill_no integer,
#             product_name text,
#             product_quantity integer,
#             product_rate integer,
#             total_price integer,
#             company_name text,
#             address text,
#             contact_number text,
#             email_address_vendor text,
#             date text
# )
# """)
# print('Table created for Data storage.')
#
# # Committing and closing the database.
# main_database.commit()
# main_database.close()

# --------------------------------------- End of Data Storage table---------------------------------------------------------#

#------------- Database for registration ------------------#

#---------------------------------------------Stock In -----------------------------------------------------------#

def stockin():
    instock = Toplevel()
    instock.title('Store Management System - Stock In')
    instock.geometry('1920x1080')
    instock.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
    instock['background'] = '#304562'

    # Creating root Frame for all sub frames
    frame = Frame(instock,bg='#304562')
    frame.grid(row=0, column=0, sticky='nsew')


    # Creating Header Frame for Title stuff ❮🠔
    header = LabelFrame(frame, height=170, width=1920, bg='#304562')
    header.grid(row=0, column=0,padx=0)


    back_home_btn = Button(header, bg='#304562', text='❮', fg='#f7f7f7', relief=FLAT, padx=20, pady=20,font=('HandVetica', 21), command = lambda : instock.destroy())
    back_home_btn.grid(row=0, column=0)

    title = Label(header, text="Store Management System", bg='#304562', fg='#f7f7f7', font=('HandVetica', 37))
    title.grid(row=0, column=1, padx=350)

    # Creating clock
    def clock():
        hour = time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000, clock)

    # Displaying time
    show_time = Label(header, bg='#304562', fg='#fbfbfb', text="", font=('digital-7', 22),padx=35)
    show_time.grid(row=0, column=2,ipadx=30 )

    clock()

    # Creating Product Details Section

    productFrame = LabelFrame(frame, height=600, pady=10,  width=500, bg='#091b33')
    productFrame.grid(row=2, column=0, padx=5, pady=40, sticky='nw')

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

# Entry fields
    billno = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman', 14))
    billno.grid(row=1, column=0, sticky='nw')

    billno_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    billno_entry.grid(row=1, column=2, padx=5, ipadx=50, ipady=10)

    productName = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Name', font=('Code New Roman', 14))
    productName.grid(row=2, column=0, pady=10, sticky='nw')

    productName_entry = Entry(productFrame,fg='#091b33',font=('Code New Roman', 10))
    productName_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    productQuantity = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Quantity',
                            font=('Code New Roman', 14))
    productQuantity.grid(row=3, column=0)

    productQuantity_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    productQuantity_entry.grid(row=3, column=2, padx=5, ipadx=50, ipady=10)

    rate = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Rate', font=('Code New Roman', 14))
    rate.grid(row=4, column=0, pady=10, sticky='nw')

    rate_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    rate_entry.grid(row=4, column=2, padx=5, ipadx=50, ipady=10)

    totalPrice = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Total Price', font=('Code New Roman', 14))
    totalPrice.grid(row=5, column=0, sticky='nw')

    totalPrice_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    totalPrice_entry.grid(row=5, column=2, padx=5, ipadx=50, ipady=10)

    # Creating Vendor Details Section

    vendorFrame = LabelFrame(frame,padx=5, pady=10, bg='#091b33',)
    vendorFrame.grid(row=2, column=0, pady=40,sticky='ne',padx=55)

    title = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text="Vendor Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    companyName = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Company Name', font=('Code New Roman', 14))
    companyName.grid(row=1, column=0, sticky='nw')

    companyName_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    companyName_entry.grid(row=1, column=2, padx=10, ipadx=50, ipady=10)

    address = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Address', font=('Code New Roman', 14))
    address.grid(row=2, column=0, pady=10, sticky='nw')

    address_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    address_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    contactNumber = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Contact Number', font=('Code New Roman', 14))
    contactNumber.grid(row=3, column=0)

    contactNumber_entry = Entry(vendorFrame, fg='#091b33',font=('Code New Roman', 10))
    contactNumber_entry.grid(row=3, column=2, padx=10, ipadx=50, ipady=10)

    email = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Email', font=('Code New Roman', 14))
    email.grid(row=4, column=0, pady=10, sticky='nw')

    email_entry = Entry(vendorFrame, fg='#091b33',font=('Code New Roman', 10))
    email_entry.grid(row=4, column=2, padx=10, ipadx=50, ipady=10)

    date = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Date', font=('Code New Roman', 14))
    date.grid(row=5, column=0, sticky='nw')

    date_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    date_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Footer frame

    footer = LabelFrame(frame,  bg='#091b33', borderwidth=0)
    footer.grid(row=3, column=0, padx=5, sticky='nw')

    description_label = Label(footer, text="Product Description", padx=10, bg='#091b33', fg='#ffffff',font=('Code New Roman', 14))
    description_label.grid(row=0, column=0, sticky="nw")

    description = Text(footer, height=11, width=71, font=('Code New Roman', 14))
    description.grid(row=1, column=0, sticky='nw')

    # Creating Add stock section frame

    add_stock_frame = LabelFrame(frame, bg='#091b33', )
    add_stock_frame.grid(row=3, column=0, padx=350, pady=40, sticky='e')

    add_stock = Button(add_stock_frame, borderwidth=0, padx=60, bg='#06e6b0', fg='#091b33', pady=30, text="Add Stock",font=('Code New Roman', 21))
    add_stock.grid(row=0, column=0, )

# --------------------------------------------- End of Stock In -----------------------------------------------------#

# -------------------------------------------- Sales ----------------------------------------------------------------#

def sales_():
    sales = Tk()
    sales.title('Store Management System - Sales')
    sales.geometry('1920x1080')
    sales.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
    sales['background'] = '#304562'

    # Creating root Frame for all sub frames
    frame = Frame(sales, bg='#304562', )
    frame.grid(row=0, column=0, sticky='nsew')

    # Creating Header Frame for Title stuff
    header = LabelFrame(frame, height=100, width=1920, bg='#304562')
    header.grid(row=0, column=0)

    back_home_btn = Button(header, bg='#304562', text='❮', fg='#f7f7f7', relief=FLAT, padx=20, pady=20,font=('HandVetica', 21), command = lambda : sales.destroy())
    back_home_btn.grid(row=0, column=0)

    title = Label(header, text="Store Management System", bg='#304562', fg='#f7f7f7', font=('HandVetica', 37))
    title.grid(row=0, column=1, padx=350)


    # Create clock
    def clock():
        hour = time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000, clock)

    # Displaying time
    show_time = Label(header, bg='#304562', fg='#f7f7f7', text="", font=('digital-7', 22),padx=50)
    show_time.grid(row=0, column=2,ipadx=30 )

    clock()

    # Creating Product Details Section

    productFrame = LabelFrame(frame, height=600, pady=10, padx=5, width=400, bg='#091b33')
    productFrame.grid(row=2, column=0, padx=5, pady=40, sticky='nw')

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    # Entry Field

    billno = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman', 14))
    billno.grid(row=1, column=0, sticky='nw')

    billno_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    billno_entry.grid(row=1, column=2, padx=5, ipadx=50, ipady=10)

    productName = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Name', font=('Code New Roman', 14))
    productName.grid(row=2, column=0, pady=10, sticky='nw')

    productName_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    productName_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    productQuantity = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Quantity',
                            font=('Code New Roman', 14))
    productQuantity.grid(row=3, column=0)

    productQuantity_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    productQuantity_entry.grid(row=3, column=2, padx=10, ipadx=50, ipady=10)

    rate = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Rate', font=('Code New Roman', 14))
    rate.grid(row=4, column=0, pady=10, sticky='nw')

    rate_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    rate_entry.grid(row=4, column=2, padx=10, ipadx=50, ipady=10)

    totalPrice = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Total Price', font=('Code New Roman', 14))
    totalPrice.grid(row=5, column=0, sticky='nw')

    totalPrice_entry = Entry(productFrame,fg='#091b33', font=('Code New Roman', 10))
    totalPrice_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Vendor Details Section

    vendorFrame = LabelFrame(frame, pady=10,padx=5,bg='#091b33')
    vendorFrame.grid(row=2, column=0,  pady=40, sticky='ne',padx=90)

    title = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text="Vendor Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    companyName = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Company Name', font=('Code New Roman', 14))
    companyName.grid(row=1, column=0, sticky='nw')

    companyName_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    companyName_entry.grid(row=1, column=2, padx=10, ipadx=50, ipady=10)

    address = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Address', font=('Code New Roman', 14))
    address.grid(row=2, column=0, pady=10, sticky='nw')

    address_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    address_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    contactNumber = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Contact Number', font=('Code New Roman', 14))
    contactNumber.grid(row=3, column=0)

    contactNumber_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    contactNumber_entry.grid(row=3, column=2, padx=10, ipadx=50, ipady=10)

    email = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Email', font=('Code New Roman', 14))
    email.grid(row=4, column=0, pady=10, sticky='nw')

    email_entry = Entry(vendorFrame,fg='#091b33', font=('Code New Roman', 10))
    email_entry.grid(row=4, column=2, padx=10, ipadx=50, ipady=10)

    date = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Date', font=('Code New Roman', 14))
    date.grid(row=5, column=0, sticky='nw')

    date_entry = Entry(vendorFrame, fg='#091b33', font=('Code New Roman', 10))
    date_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Add stock section frame

    add_stock_frame = LabelFrame(frame, bg='#091b33', )
    add_stock_frame.grid(row=3, column=0, padx=350, pady=40, )

    add_stock = Button(add_stock_frame, borderwidth=0, padx=95, bg='#06e6b0', fg='#091b33', pady=30, text="Sales",font=('Code New Roman', 21))
    add_stock.grid(row=0, column=0, )

# -------------------------------------------- End of sales --------------------------------------------------------#

# ---------------------------------------------- Update ------------------------------------------------------------#

def update_():
    update = Toplevel()
    update.title('Store Management System - Update')
    update.geometry('1920x1080')
    update.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
    update['background'] = '#304562'

    # Creating root Frame for all sub frames
    frame = Frame(update, bg='#304562', )
    frame.grid(row=0, column=0, sticky='nsew')

    # Creating Header Frame for Title stuff
    header = LabelFrame(frame, height=100, width=1920, bg='#304562')
    header.grid(row=0, column=0)

    back_home_btn = Button(header, bg='#304562', text='❮', relief=FLAT,  fg='#f7f7f7',padx=20, pady=20,font=('HandVetica', 21), command = lambda : update.destroy())
    back_home_btn.grid(row=0, column=0)

    title = Label(header, text="Store Management System", bg='#304562', fg='#f7f7f7', font=('HandVetica', 37))
    title.grid(row=0, column=1, padx=350)

    # Creating clock
    def clock():
        hour = time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000, clock)

    # Displaying time
    show_time = Label(header, bg='#304562', fg='#f7f7f7', text="", font=('digital-7', 22), padx=50)
    show_time.grid(row=0, column=2, ipadx=30)

    clock()

    # Creating Product Details Section

    productFrame = LabelFrame(frame, height=600, pady=10, padx=10, width=800, bg='#091b33')
    productFrame.grid(row=2, column=0, padx=20, pady=40, sticky='nw')

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    billno = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman', 14))
    billno.grid(row=1, column=0, sticky='nw')

    billno_entry = Entry(productFrame)
    billno_entry.grid(row=1, column=2, padx=10, ipadx=50, ipady=10)

    productName = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Name', font=('Code New Roman', 14))
    productName.grid(row=2, column=0, pady=10, sticky='nw')

    productName_entry = Entry(productFrame)
    productName_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    productQuantity = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Quantity',font=('Code New Roman', 14))
    productQuantity.grid(row=3, column=0)

    productQuantity_entry = Entry(productFrame)
    productQuantity_entry.grid(row=3, column=2, padx=10, ipadx=50, ipady=10)

    rate = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Rate', font=('Code New Roman', 14))
    rate.grid(row=4, column=0, pady=10, sticky='nw')

    rate_entry = Entry(productFrame)
    rate_entry.grid(row=4, column=2, padx=10, ipadx=50, ipady=10)

    totalPrice = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Total Price', font=('Code New Roman', 14))
    totalPrice.grid(row=5, column=0, sticky='nw')

    totalPrice_entry = Entry(productFrame)
    totalPrice_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Vendor Details Section

    vendorFrame = LabelFrame(frame,  pady=10, padx=5, bg='#091b33')
    vendorFrame.grid(row=2, column=0, padx=90, pady=40, sticky='ne')

    title = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text="Vendor Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    companyName = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Company Name', font=('Code New Roman', 14))
    companyName.grid(row=1, column=0, sticky='nw')

    companyName_entry = Entry(vendorFrame)
    companyName_entry.grid(row=1, column=2, padx=10, ipadx=50, ipady=10)

    address = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Address', font=('Code New Roman', 14))
    address.grid(row=2, column=0, pady=10, sticky='nw')

    address_entry = Entry(vendorFrame)
    address_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    contactNumber = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Contact Number', font=('Code New Roman', 14))
    contactNumber.grid(row=3, column=0)

    contactNumber_entry = Entry(vendorFrame)
    contactNumber_entry.grid(row=3, column=2, padx=10, ipadx=50, ipady=10)

    email = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Email', font=('Code New Roman', 14))
    email.grid(row=4, column=0, pady=10, sticky='nw')

    email_entry = Entry(vendorFrame)
    email_entry.grid(row=4, column=2, padx=10, ipadx=50, ipady=10)

    date = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Date', font=('Code New Roman', 14))
    date.grid(row=5, column=0, sticky='nw')

    date_entry = Entry(vendorFrame, )
    date_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Add stock section frame

    add_stock_frame = LabelFrame(frame, bg='#091b33', )
    add_stock_frame.grid(row=3, column=0, padx=350, pady=40, )

    add_stock = Button(add_stock_frame, borderwidth=0, padx=90, bg='#06e6b0', fg='#091b33', pady=30, text="Update",font=('Code New Roman', 21))
    add_stock.grid(row=0, column=0, )

# ----------------------------------------- End of Update ----------------------------------------------------------#

# ---------------------------------------- DASHBOARD WINDOW --------------------------------------------------------#

# # Defining window
def dashboard():

    dashboard_page = Toplevel()
    dashboard_page.geometry('1920x1080')
    dashboard_page.title('Store Management System - Dashboard')
    dashboard_page['background'] = '#304562'
    dashboard_page.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')

    # Creating root Frame for all sub frames
    frame = Frame(dashboard_page,bg='#304562',)
    frame.grid(row=0, column=0, sticky='nsew')


    # Creating Header Frame for Title stuff
    header = LabelFrame(frame, height=100, width=1930,bg='#304562',)
    header.grid(row=0, column=0,ipadx=20)

    # Using logo
    logo = ImageTk.PhotoImage(Image.open("C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store-white.png"))
    logo_icon = Label(header,bg='#304562',fg='#f7f7f7',image=logo)
    logo_icon.grid(row=0, column=0, padx=5,ipadx=25, pady=5)

    # Heading Title
    title = Label(header, bg='#304562',fg='#f7f7f7',text="Store Management System",font=('HandVetica',37))
    title.grid(row=0, column=1, padx=340)

    # Creating clock
    def clock():
        hour= time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000,clock)

    # Displaying time

    show_time = Label(header,bg='#304562',fg='#fbfbfb', text="",font=('digital-7', 22))
    show_time.grid(row=0, column=2,ipadx=30)

    clock()

    # Creating Menu Frame for sub Button
    menu = LabelFrame(frame,pady=23, padx=80,bg='#091b33',borderwidth=0)
    menu.grid(row=1,column=0,sticky= NW,)

    # Buttons for sub page
    stock_in = Button(menu,padx=50,pady=30,text='Stock In',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",command=stockin)
    stock_in.grid(row=0,column=0,padx=60,pady=17,ipady=15)

    sales = Button(menu,padx=72,pady=30, text='Sales',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",command=sales_)
    sales.grid(row=1,column=0,padx=50,ipady=15,pady=15)

    update = Button(menu,padx=63,pady=30, text='Update',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",command=update_)
    update.grid(row=2,column=0,padx=50,ipady=15,pady=15)

    total = Button(menu,padx=70,pady=30, text='Total',font=('Code New Roman',21),bg="#06e6b0",fg="#091b33",)
    total.grid(row=3,column=0,padx=52,ipady=15,pady=17)

    # Creating frame for date and logout section

    sub_header = LabelFrame(frame,bg='#304562',borderwidth=0)
    sub_header.grid(row=1,column=0,columnspan=2,sticky=NE,ipady=10,)

    def date():
        year = time.strftime('%Y')
        month = time.strftime('%b')
        day = time.strftime('%d')

        date_sec.config(text=year + ' ' + month + ' ' + day)
        date_sec.after(1000, date)

    # For displaying date
    date_sec = Label(sub_header, fg='#f7f7f7', bg='#304562', font=('digital-7',21))
    date_sec.grid(row=0, column=0,ipady=10, sticky=NW, padx=300)

    date()

    def logout():
        askk = messagebox.askokcancel('Logout', 'Do you want to logout ?')
        if askk == 'ok':
            dashboard_page.destroy()
        else:
            dashboard_page.mainloop()



    # Button with icon for logout
    icon_logout = ImageTk.PhotoImage(Image.open('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/logout-white.png'))
    logout_btn = Button(sub_header, bg='#304562',image=icon_logout,  relief=FLAT, command= logout)
    logout_btn.grid(row=0,column=3,padx=100,ipady=12)

    # Creating frame for calculator section

    # Creating main frame for calculator
    calcFrame = LabelFrame(frame,bg='#091b33',borderwidth=0,padx=27,pady=15)
    calcFrame.grid(row=1, column=0,sticky=NE,padx=210,pady=200)

    # Creating input field
    inputField = Entry(calcFrame, width=55, bg="#fbfbfb",font=('Code New Roman',14))
    inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10,ipadx=20, ipady=17)

    # Creating functions for calculator
    # For showing entered number

    def click_button(number):
        current_value = inputField.get()
        inputField.delete(0, END)
        inputField.insert(0, str(current_value) + str(number))

    # To clear entered input
    def clear_button():
        inputField.delete(0, END)

    # To shut the project
    def power_off():
        return
        # popup = tkinter.messagebox.askokcancel('Close', 'Calculator window will be disappeared.')
        # if popup == True:
        #     calcFrame.destroy()
        # else:
        #     calcFrame.mainloop()

    # For adding numbers
    def button_add():
        first_number = inputField.get()
        global num_first
        global calculation
        calculation = 'addition'
        num_first= int(first_number)
        inputField.delete(0, END)

    # To get result
    def button_equal():
        second_number = inputField.get()
        inputField.delete(0, END)
        if calculation == "addition":
            inputField.insert(0, num_first + int(second_number))
        elif calculation == "subtraction":
            inputField.insert(0, num_first - int(second_number))
        elif calculation == "division":
            inputField.insert(0, num_first // int(second_number))
        elif calculation == "multiplication":
            inputField.insert(0, num_first * int(second_number))

    # To subtract
    def button_subtract():
        first_number = inputField.get()
        global num_first
        global calculation
        calculation = 'subtraction'
        num_first= int(first_number)
        inputField.delete(0, END)

    # To multiply
    def button_multiply():
        first_number = inputField.get()
        global num_first
        global calculation
        calculation = 'multiplication'
        num_first= int(first_number)
        inputField.delete(0, END)

    # To divide
    def button_divide():
        first_number = inputField.get()
        global num_first
        global calculation
        calculation = 'division'
        num_first= int(first_number)
        inputField.delete(0, END)


    # # Creating numeric buttons
    button_0 = Button(calcFrame, text="0", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(0) )
    button_1 = Button(calcFrame, text="1", padx=43, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(1) )
    button_2 = Button(calcFrame, text="2", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(2) )
    button_3 = Button(calcFrame, text="3", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(3) )
    button_4 = Button(calcFrame, text="4", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(4) )
    button_5 = Button(calcFrame, text="5", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(5) )
    button_6 = Button(calcFrame, text="6", padx=45, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(6) )
    button_7 = Button(calcFrame, text="7", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(7) )
    button_8 = Button(calcFrame, text="8", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(8) )
    button_9 = Button(calcFrame, text="9", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15),command =lambda: click_button(9) )

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
    button_add = Button(calcFrame, text="➕", padx=32, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,),command=button_add )
    button_sub = Button(calcFrame, text="−", padx=41, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,),command=button_subtract )
    button_mul = Button(calcFrame, text="x", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,),command= button_multiply)
    button_div = Button(calcFrame, text="÷", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,),command= button_divide)
    button_equal = Button(calcFrame, text="=", padx=163, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,),command=button_equal )

    # Putting calculation buttons on screen
    button_add.grid(row=1, column=1, padx=5, pady=5)
    button_sub.grid(row=1, column=2, padx=5, pady=5)
    button_mul.grid(row=4, column=0, padx=0, pady=5)
    button_div.grid(row=4, column=1, padx=9, pady=5)
    button_equal.grid(row=4, column=2, columnspan=3, padx=5, pady=5)

    # Creating special buttons
    button_clear = Button(calcFrame, text="C", padx=40, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15, "bold"),command=clear_button )
    button_off = Button(calcFrame, text="Off", padx=90, pady=20, bg="#304562", fg="#f0ece2",relief=FLAT, font=('Code New Roman', 15,),command=power_off,stat =DISABLED )

    # Putting special buttons on screen
    button_clear.grid(row=1, column=0, padx=5, pady=5)
    button_off.grid(row=1, column=3, columnspan=2, padx=5, pady=5)


    dashboard_page.mainloop()


def register():
    main_database = sqlite3.connect('storemanagement.db')
    c = main_database.cursor()

    c.execute("INSERT INTO authentication VALUES(:first_name,:last_name,:email_address,:username,:password)", {
              'first_name': firstname_entry.get(),
              'last_name': lastname_entry.get(),
              'email_address': email_entry.get(),
              'username': username_entry.get(),
              'password': password_entry.get()
    })

    main_database.commit()
    main_database.close()

    if firstname_entry.get() == "" or lastname_entry.get() == "" or email_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error", "Please fill all data.")
    else:
        messagebox.showinfo("Success", "Registration Successful")
    # To clear screen after submission

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

#------------- END of  Database for registration ------------------#  WHERE username ={name_entry.get()} and password ={passw_entry.get()}

def signup():
    global firstname_entry
    global lastname_entry
    global email_entry
    global username_entry
    global password_entry

    signup_setup= Toplevel()
    signup_setup.geometry('1920x1080')
    signup_setup.title(' Store Management System - Signup')
    signup_setup['background'] = '#304562'

    signup_setup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

    loginBox = LabelFrame(signup_setup, borderwidth=0, bg="#091b33", height=900, width=500, )
    loginBox.grid(row=0, column=0, padx=500, pady=30)

    firstname_label = Label(loginBox, text='First Name', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",font=('Code New Roman', 21))
    firstname_entry = Entry(loginBox, font=('helvetica', 14))
    firstname_label.grid(row=0, column=0, padx=100, pady=10)
    firstname_entry.grid(row=1, column=0, ipadx=50, ipady=10)

    lastname_label = Label(loginBox, text='Last Name', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",font=('Code New Roman', 21))
    lastname_entry = Entry(loginBox,  font=('helvetica', 14))
    lastname_label.grid(row=2, column=0, padx=100, pady=10)
    lastname_entry.grid(row=3, column=0, ipadx=50, ipady=10)

    email_label = Label(loginBox, text='Email', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",font=('Code New Roman', 21))
    email_entry = Entry(loginBox,  font=('helvetica', 14))
    email_label.grid(row=4, column=0, padx=100, pady=10)
    email_entry.grid(row=5, column=0, ipadx=50, ipady=10)

    username_label = Label(loginBox, text='Username', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",font=('Code New Roman', 21))
    username_entry = Entry(loginBox, font=('helvetica', 14))
    username_label.grid(row=6, column=0, padx=100, pady=10)
    username_entry.grid(row=7, column=0, ipadx=50, ipady=10)

    password_label = Label(loginBox, text="Password", bg="#091b33", padx=60, pady=15, fg="#f7f7f7",font=('Code New Roman', 21))
    password_entry = Entry(loginBox,  show='*', font=('helvetica', 14))
    password_label.grid(row=8, column=0, padx=100, pady=10)
    password_entry.grid(row=9, column=0, ipadx=50, ipady=10)

    sub_btn = Button(loginBox, text='Sign Up', bg="#06e6b0", fg="#091b33", font=('Code New Roman', 21),command=register)
    sub_btn.grid(row=10, column=0, pady=25, ipadx=40, ipady=7)

#  --------------------------------- END of Signup Page -------------------------------------#

def login():
    global user_name
    global pass_word

    main_database = sqlite3.connect('storemanagement.db')
    c = main_database.cursor()

    c.execute("SELECT * FROM authentication ")
    datas = c.fetchall()
    u_name = name_entry.get()
    pas = passw_entry.get()

    # Loop through the results
    user_name_store = ''
    pass_word_store = ''

    for record in datas:
        user_name_store += str(record[3])
        pass_word_store += str(record[4])

    if name_entry.get() == "" or passw_entry.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password")
    else:
        if u_name in user_name_store and pas in pass_word_store:
            name_entry.delete(0, END)
            passw_entry.delete(0, END)
            # messagebox.showinfo("Success", "Successfully Login")
            dashboard()

        else:
            messagebox.showerror("Error", "Invalid Username and Password")

    main_database.commit()
    main_database.close()

#  --------------------------------- Login Page --------------------------------------------#

def home_login():
    global name_entry
    global passw_entry
    login_setup = Toplevel()
    login_setup.geometry('1920x1080')
    login_setup.title('Login')
    login_setup['background'] = '#304562'

    login_setup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

    loginBox = LabelFrame(login_setup,borderwidth=0, bg="#091b33",height=500,width=500,)
    loginBox.grid(row=0,column=0,padx=500,pady=150)

    name_label = Label(loginBox, text='Username',bg="#091b33",padx=60,pady=20,fg="#f7f7f7", font=('Code New Roman',21))
    name_entry = Entry(loginBox, font=('helvetica', 14))
    name_label.grid(row=0, column=0, padx=100, pady=10)
    name_entry.grid(row=1, column=0, ipadx=50, ipady=10)

    passw_label = Label(loginBox, text="Password",bg="#091b33",padx=60,pady=20,fg="#f7f7f7", font=('Code New Roman', 21))
    passw_entry = Entry(loginBox,  show='*', font=('helvetica', 14))
    passw_label.grid(row=2, column=0, padx=100, pady=10)
    passw_entry.grid(row=3, column=0, ipadx=50, ipady=10)

    login_btn = Button(loginBox, text=' Login ' ,bg="#06e6b0",fg="#091b33", font=('Code New Roman', 21),command=login)
    login_btn.grid(row=4, column=0,pady=25, ipadx=50, ipady=4)

    register_btn = Button(loginBox,text='Register' ,bg="#06e6b0",fg="#091b33", font=('Code New Roman', 21),command=signup)
    register_btn.grid(row=5, column=0,pady=25, ipadx=40, ipady=4)

    login_setup.mainloop()


global name_entry
global passw_entry
login_setup = Tk()
login_setup.geometry('1920x1080')
login_setup.title('Login')
login_setup['background'] = '#304562'

login_setup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

loginBox = LabelFrame(login_setup,borderwidth=0, bg="#091b33",height=500,width=500,)
loginBox.grid(row=0,column=0,padx=500,pady=150)

name_label = Label(loginBox, text='Username',bg="#091b33",padx=60,pady=20,fg="#f7f7f7", font=('Code New Roman',21))
name_entry = Entry(loginBox, font=('helvetica', 14))
name_label.grid(row=0, column=0, padx=100, pady=10)
name_entry.grid(row=1, column=0, ipadx=50, ipady=10)

passw_label = Label(loginBox, text="Password",bg="#091b33",padx=60,pady=20,fg="#f7f7f7", font=('Code New Roman', 21))
passw_entry = Entry(loginBox,  show='*', font=('helvetica', 14))
passw_label.grid(row=2, column=0, padx=100, pady=10)
passw_entry.grid(row=3, column=0, ipadx=50, ipady=10)

login_btn = Button(loginBox, text=' Login ' ,bg="#06e6b0",fg="#091b33", font=('Code New Roman', 21),command=login)
login_btn.grid(row=4, column=0,pady=25, ipadx=50, ipady=4)

register_btn = Button(loginBox,text='Register', bg="#06e6b0",fg="#091b33", font=('Code New Roman', 21),command=signup)
register_btn.grid(row=5, column=0,pady=25, ipadx=40, ipady=4)

login_setup.mainloop()
