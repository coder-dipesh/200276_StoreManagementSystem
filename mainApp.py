# Importing necessary module
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from tkinter import ttk


# -------------------------------------Creating database table --------------------------------------------------------#

# Creating databases with sub table

# --------------------------------------- Authentication Table --------------------------------------------------------#
# # Database queries for Authentication
# # # Giving database name
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

# Committing and closing the database.
# main_database.commit()
# main_database.close()

# --------------------------------------- End of authentication table------------------------------------------------#

# ---------------------------------------  Data storage table -------------------------------------------------------#
# Database queries for Data storage
# # Giving database name
# main_database = sqlite3.connect('storemanagement.db')
#
# # # Initializing cursor
# c = main_database.cursor()
#  # Creating authentication table
# c.execute("""CREATE TABLE data_storage(
#              bill_no integer,
#              product_name text,
#              product_quantity integer,
#              product_rate integer,
#              total_price integer,
#              company_name text,
#              address text,
#              contact_number text,
#              email_address_vendor text,
#              date text,
#              description text
#   )
#   """)
# print('Table created for Data storage.')
#
# # Committing and closing the database.
# main_database.commit()
# main_database.close()


# --------------------------------------- End of Data Storage table-----------------------------------------------#

# ------------- Database for registration ------------------#

# def popup():
#     messagebox.showinfo('Added','Successfully')


# ---------------------------------------------Stock In -----------------------------------------------------------#

def stockin():
    global billno_entry
    global productName_entry
    global productQuantity_entry
    global rate_entry
    global totalPrice_entry
    global companyName_entry
    global address_entry
    global contactNumber_entry
    global date_entry
    global email_entry
    global description_entry
    global instock

    instock = Toplevel()
    instock.title('Store Management System - Stock In')
    instock.geometry('1920x1080')
    instock.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
    instock['background'] = '#304562'

    # Creating root Frame for all sub frames
    frame = Frame(instock, bg='#304562')
    frame.grid(row=0, column=0, sticky='nsew')

    # Creating Header Frame for Title stuff ❮🠔
    header = LabelFrame(frame, height=170, width=1920, bg='#304562')
    header.grid(row=0, column=0, padx=0)

    back_home_btn = Button(header, bg='#304562', text='❮', fg='#f7f7f7', relief=FLAT, padx=20, pady=20,
                           font=('HandVetica', 21), command=lambda: instock.destroy())
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
    show_time = Label(header, bg='#304562', fg='#fbfbfb', text="", font=('digital-7', 22), padx=35)
    show_time.grid(row=0, column=2, ipadx=30)

    clock()

    # Creating Product Details Section

    productFrame = LabelFrame(frame, height=600, pady=10, width=500, bg='#091b33')
    productFrame.grid(row=2, column=0, padx=5, pady=40, sticky='nw')

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    # Entry fields
    billno = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman', 14))
    billno.grid(row=1, column=0, sticky='nw')

    billno_entry = Entry(productFrame, fg='#091b33', font=('Code New Roman', 10))
    billno_entry.focus()
    billno_entry.grid(row=1, column=2, padx=5, ipadx=50, ipady=10)

    productName = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Name', font=('Code New Roman', 14))
    productName.grid(row=2, column=0, pady=10, sticky='nw')

    productName_entry = Entry(productFrame, fg='#091b33', font=('Code New Roman', 10))
    productName_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    productQuantity = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Quantity',
                            font=('Code New Roman', 14))
    productQuantity.grid(row=3, column=0)

    productQuantity_entry = Entry(productFrame, fg='#091b33', font=('Code New Roman', 10))
    productQuantity_entry.grid(row=3, column=2, padx=5, ipadx=50, ipady=10)

    rate = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Rate', font=('Code New Roman', 14))
    rate.grid(row=4, column=0, pady=10, sticky='nw')

    rate_entry = Entry(productFrame, fg='#091b33', font=('Code New Roman', 10))
    rate_entry.grid(row=4, column=2, padx=5, ipadx=50, ipady=10)

    totalPrice = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Total Price', font=('Code New Roman', 14))
    totalPrice.grid(row=5, column=0, sticky='nw')

    totalPrice_entry = Entry(productFrame, fg='#091b33', font=('Code New Roman', 10))
    totalPrice_entry.grid(row=5, column=2, padx=5, ipadx=50, ipady=10)

    # Creating Vendor Details Section

    vendorFrame = LabelFrame(frame, padx=5, pady=10, bg='#091b33', )
    vendorFrame.grid(row=2, column=0, pady=40, sticky='ne', padx=55)

    title = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text="Vendor Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    companyName = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Company Name', font=('Code New Roman', 14))
    companyName.grid(row=1, column=0, sticky='nw')

    companyName_entry = Entry(vendorFrame, fg='#091b33', font=('Code New Roman', 10))
    companyName_entry.grid(row=1, column=2, padx=10, ipadx=50, ipady=10)

    address = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Address', font=('Code New Roman', 14))
    address.grid(row=2, column=0, pady=10, sticky='nw')

    address_entry = Entry(vendorFrame, fg='#091b33', font=('Code New Roman', 10))
    address_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    contactNumber = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Contact Number', font=('Code New Roman', 14))
    contactNumber.grid(row=3, column=0)

    contactNumber_entry = Entry(vendorFrame, fg='#091b33', font=('Code New Roman', 10))
    contactNumber_entry.grid(row=3, column=2, padx=10, ipadx=50, ipady=10)

    email = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Email', font=('Code New Roman', 14))
    email.grid(row=4, column=0, pady=10, sticky='nw')

    email_entry = Entry(vendorFrame, fg='#091b33', font=('Code New Roman', 10))
    email_entry.grid(row=4, column=2, padx=10, ipadx=50, ipady=10)

    date = Label(vendorFrame, bg='#091b33', fg='#f7f7f7', text='Date', font=('Code New Roman', 14))
    date.grid(row=5, column=0, sticky='nw')

    date_entry = Entry(vendorFrame, fg='#091b33', font=('Code New Roman', 10))
    date_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Footer frame

    footer = LabelFrame(frame, bg='#091b33', borderwidth=0)
    footer.grid(row=3, column=0, padx=5, sticky='nw')

    description_label = Label(footer, text="Product Description", padx=10, bg='#091b33', fg='#ffffff',
                              font=('Code New Roman', 14))
    description_label.grid(row=0, column=0, sticky="nw")

    description_entry = Text(footer, height=11, width=71, font=('Code New Roman', 14))
    description_entry.grid(row=1, column=0, sticky='nw')

    # Creating Add stock section frame

    add_stock_frame = LabelFrame(frame, bg='#091b33', )
    add_stock_frame.grid(row=3, column=0, padx=350, pady=40, sticky='e')

    add_stock = Button(add_stock_frame, borderwidth=0, padx=60, bg='#06e6b0', fg='#091b33', pady=30, text="Add Stock",
                       font=('Code New Roman', 21), command=lambda:[stockin_data(), showinfo()])
    add_stock.grid(row=0, column=0, )


def showinfo():
    messagebox.showinfo('Added','Data added successfully', parent=instock)

# --------------------------------------------- End of Stock In -----------------------------------------------------#

# ------------------------------------------Adding into Database----------------------------------------------------#

def stockin_data():
    main_database = sqlite3.connect('storemanagement.db')

    c = main_database.cursor()

    # Adding to database
    c.execute(
        "INSERT INTO data_storage VALUES(:bill_no, :product_name,:product_quantity,:product_rate,:total_price,:company_name,:address,:contact_number,:email_address_vendor,:date,:description)",
        {
            'bill_no': billno_entry.get(),
            'product_name': productName_entry.get(),
            'product_quantity': productQuantity_entry.get(),
            'product_rate': rate_entry.get(),
            'total_price': totalPrice_entry.get(),
            'company_name': companyName_entry.get(),
            'address': address_entry.get(),
            'contact_number': contactNumber_entry.get(),
            'email_address_vendor': email_entry.get(),
            'date': date_entry.get(),
            'description': description_entry.get('1.0', 'end-1c')

        })

    print('added sucessfully')

    main_database.commit()
    main_database.close()

    billno_entry.delete(0, END)
    productName_entry.delete(0, END)
    productQuantity_entry.delete(0, END)
    rate_entry.delete(0, END)
    totalPrice_entry.delete(0, END)
    companyName_entry.delete(0, END)
    address_entry.delete(0, END)
    contactNumber_entry.delete(0, END)
    date_entry.delete(0, END)
    email_entry.delete(0,END)
    description_entry.delete('1.0', END)

# ------------------------------------------End of Adding into Database---------------------------------------------#

# -------------------------------------------- Sales ----------------------------------------------------------------#

def sales_():
    global billno_entry_
    global sales

    sales = Toplevel()
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

    back_home_btn = Button(header, bg='#304562', text='❮', fg='#f7f7f7', relief=FLAT, padx=20, pady=20,
                           font=('HandVetica', 21), command=lambda: sales.destroy())
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
    show_time = Label(header, bg='#304562', fg='#f7f7f7', text="", font=('digital-7', 22), padx=50)
    show_time.grid(row=0, column=2, ipadx=30)

    clock()

    # Creating Product Details Section

    productFrame = LabelFrame(frame, height=600, pady=10, padx=5, width=400, bg='#091b33')
    productFrame.grid(row=2, column=0, padx=5, pady=40, )

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    # Entry Field

    billno = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman', 14))
    billno.grid(row=1, column=0, sticky='nw')

    billno_entry_ = Entry(productFrame, fg='#091b33', font=('Code New Roman', 10))
    billno_entry_.focus()
    billno_entry_.grid(row=1, column=2, padx=5, ipadx=50, ipady=10)


    # Creating Sales stock section frame

    sales_stock_frame = LabelFrame(frame, bg='#091b33')
    sales_stock_frame.grid(row=3, column=0, padx=350, pady=40)

    sales_stock = Button(sales_stock_frame, borderwidth=0, padx=95, bg='#06e6b0', fg='#091b33', pady=30, text="Sales",
                         font=('Code New Roman', 21) , command=lambda: [sales_data() , message()])
    sales_stock.grid(row=0, column=0, )

def message():
    messagebox.showinfo('Removed' , 'Data Deleted successfully.', parent=sales)
# -------------------------------------------- End of sales --------------------------------------------------------#

# -------------------------------------------- sales data -----------------------------------------------------#

def sales_data():
    main_database = sqlite3.connect('storemanagement.db')

    c = main_database.cursor()

    c.execute("DELETE from data_storage WHERE bill_no = " + billno_entry_.get())

    billno_entry_.delete(0, END)



    main_database.commit()
    main_database.close()



# -------------------------------------------- End of sales data -----------------------------------------------------#

# ---------------------------------------------- Update ------------------------------------------------------------#

def update_():
    global billno_entry
    global update

    update = Toplevel()
    update.title('Store Management System - Update')
    update.geometry('1920x1080')
    update.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
    update['background'] = '#304562'

    # Creating root Frame for all sub frames
    frame = Frame(update, bg='#304562',)
    frame.grid(row=0, column=0, sticky='nsew')

    # Creating Header Frame for Title stuff
    header = LabelFrame(frame, height=100, width=1920, bg='#304562')
    header.grid(row=0, column=0)

    back_home_btn = Button(header, bg='#304562', text='❮', relief=FLAT, fg='#f7f7f7', padx=20, pady=20,
                           font=('HandVetica', 21), command=lambda: update.destroy())
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
    productFrame.grid(row=2, column=0, padx=20, pady=40, )

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    billno = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Bill No', font=('Code New Roman', 14))
    billno.grid(row=1, column=0, sticky='nw')

    billno_entry = Entry(productFrame)
    billno_entry.focus()
    billno_entry.grid(row=1, column=2, padx=10, ipadx=50, ipady=10)

    # Creating Add stock section frame

    update_stock_frame = LabelFrame(frame, bg='#091b33', )
    update_stock_frame.grid(row=3, column=0, padx=350, pady=40, )

    update_stock = Button(update_stock_frame, borderwidth=0, padx=90, bg='#06e6b0', fg='#091b33', pady=30, text="Update",font=('Code New Roman', 21),command=update_data )
    update_stock.grid(row=0, column=0,)


def update_data():
    global data_update_popup
    global productName_entry
    global productQuantity_entry
    global rate_entry
    global totalPrice_entry
    global companyName_entry
    global address_entry
    global contactNumber_entry
    global email_entry
    global date_entry
    global key_value

    data_update_popup = Toplevel()
    data_update_popup.title('Store Management System - Update')
    data_update_popup.geometry('800x1000')
    data_update_popup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')
    data_update_popup['background'] = '#304562'


    main_database = sqlite3.connect('storemanagement.db')

    # c = main_database.cursor()
    cursor = main_database.cursor()

    key_value = billno_entry.get()
    print(key_value)

    cursor.execute("SELECT * FROM data_storage WHERE bill_no = "+ key_value)

    infos = cursor.fetchall()

    print(infos)

    billno_entry.delete(0, END)

    #Design for popup
    frame = Frame(data_update_popup, bg='#304562', )
    frame.grid(row=0, column=0, sticky='nsew')

    productFrame = LabelFrame(frame, height=600, pady=10, padx=10, width=800, bg='#091b33')
    productFrame.grid(row=0, column=0, padx=20, pady=40, sticky='n')

    title = Label(productFrame, bg='#091b33', fg='#f7f7f7', text="Product Details", font=('Code New Roman', 14))
    title.grid(row=0, column=1, padx=70)

    productName = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Name', font=('Code New Roman', 14))
    productName.grid(row=2, column=0, pady=10, sticky='nw')

    productName_entry = Entry(productFrame)
    productName_entry.focus()
    productName_entry.grid(row=2, column=2, ipadx=50, ipady=10)

    productQuantity = Label(productFrame, bg='#091b33', fg='#f7f7f7', text='Product Quantity',
                            font=('Code New Roman', 14))
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

    vendorFrame = LabelFrame(frame, pady=10, padx=10, bg='#091b33')
    vendorFrame.grid(row=1, column=0, padx=20, pady=40,sticky='s')

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

    date_entry = Entry(vendorFrame)
    date_entry.grid(row=5, column=2, padx=10, ipadx=50, ipady=10)

    for data in infos:
        productName_entry.insert(0, data[1])
        productQuantity_entry.insert(0, data[2])
        rate_entry.insert(0, data[3])
        totalPrice_entry.insert(0, data[4])
        companyName_entry.insert(0, data[5])
        address_entry.insert(0, data[6])
        contactNumber_entry.insert(0, data[7])
        email_entry.insert(0, data[8])
        date_entry.insert(0, data[9])



    save = Button(frame, text='SAVE', font=('Code New Roman', 21), bg="#06e6b0", fg="#091b33",
                  command= lambda :[after_update(),update_message()])
    save.grid(row=6, columnspan=5, column=0, ipady=10, ipadx=105)


def after_update():
    main_database = sqlite3.connect('storemanagement.db')

    c = main_database.cursor()

    record_id = billno_entry.get()

#Must be same name as in database
    c.execute("""UPDATE data_storage SET        
                product_name = :productN,
                product_quantity = :productQ,
                product_rate = :rate,
                total_price =:total,
                company_name =:companyN,
                address =:address,
                email_address_vendor =:email_address,
                contact_number= :number,
                date= :date
                WHERE bill_no = :bill_no""",

              {
                'productN': productName_entry.get(),
                'productQ': productQuantity_entry.get(),
                'rate': rate_entry.get(),
                'total': totalPrice_entry.get(),
                'companyN': companyName_entry.get(),
                'address': address_entry.get(),
                'email_address': email_entry.get(),
                'number': contactNumber_entry.get(),
                'date': date_entry.get(),
                'bill_no': key_value

              }
    )

    print('Updated Successfully')

    main_database.commit()
    main_database.close()

    data_update_popup.destroy()


def update_message():
    messagebox.showinfo('Updated', 'Data Updated Successfully. You can view at Total section.', parent=update)

# ----------------------------------------- End of Update ----------------------------------------------------------#

# ---------------------------------------- DASHBOARD WINDOW --------------------------------------------------------#

def dashboard():
    dashboard_page = Toplevel()
    dashboard_page.geometry('1920x1080')
    dashboard_page.title('Store Management System - Dashboard')
    dashboard_page['background'] = '#304562'
    dashboard_page.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')

    # Creating root Frame for all sub frames
    frame = Frame(dashboard_page, bg='#304562', )
    frame.grid(row=0, column=0, sticky='nsew')

    # Creating Header Frame for Title stuff
    header = LabelFrame(frame, height=100, width=1930, bg='#304562', )
    header.grid(row=0, column=0, ipadx=20)

    # Using logo
    logo = ImageTk.PhotoImage(Image.open("C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store-white.png"))
    logo_icon = Label(header, bg='#304562', fg='#f7f7f7', image=logo)
    logo_icon.grid(row=0, column=0, padx=5, ipadx=25, pady=5)

    # Heading Title
    title = Label(header, bg='#304562', fg='#f7f7f7', text="Store Management System", font=('HandVetica', 37))
    title.grid(row=0, column=1, padx=340)

    # Creating clock
    def clock():
        hour = time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000, clock)

    # Displaying time

    show_time = Label(header, bg='#304562', fg='#fbfbfb', text="", font=('digital-7', 22))
    show_time.grid(row=0, column=2, ipadx=30)

    clock()

    # Creating Menu Frame for sub Button
    menu = LabelFrame(frame, pady=23, padx=80, bg='#091b33', borderwidth=0)
    menu.grid(row=1, column=0, sticky=NW, )

    # Buttons for sub page
    stock_in = Button(menu, padx=50, pady=30, text='Stock In', font=('Code New Roman', 21), bg="#06e6b0", fg="#091b33",
                      command=stockin)
    stock_in.grid(row=0, column=0, padx=60, pady=17, ipady=15)

    sales = Button(menu, padx=72, pady=30, text='Sales', font=('Code New Roman', 21), bg="#06e6b0", fg="#091b33",
                   command=sales_)
    sales.grid(row=1, column=0, padx=50, ipady=15, pady=15)

    update = Button(menu, padx=63, pady=30, text='Update', font=('Code New Roman', 21), bg="#06e6b0", fg="#091b33",
                    command=update_)
    update.grid(row=2, column=0, padx=50, ipady=15, pady=15)

    total = Button(menu, padx=70, pady=30, text='Total', font=('Code New Roman', 21), bg="#06e6b0", fg="#091b33",command=show_total)
    total.grid(row=3, column=0, padx=52, ipady=15, pady=17)

    # Creating frame for date and logout section

    sub_header = LabelFrame(frame, bg='#304562', borderwidth=0)
    sub_header.grid(row=1, column=0, columnspan=2, sticky=NE, ipady=10, )

    def date():
        year = time.strftime('%Y')
        month = time.strftime('%b')
        day = time.strftime('%d')

        date_sec.config(text=year + ' ' + month + ' ' + day)
        date_sec.after(1000, date)

    # For displaying date
    date_sec = Label(sub_header, fg='#f7f7f7', bg='#304562', font=('digital-7', 21))
    date_sec.grid(row=0, column=0, ipady=10, sticky=NW, padx=300)

    date()

    def log_out():
        message = messagebox.askquestion('Logout', 'Do you want to logout ?',parent=dashboard_page)
        if message == 'yes':
            dashboard_page.destroy()
        elif message =='no':
            dashboard_page.mainloop()



    # Button with icon for logout
    icon_logout = ImageTk.PhotoImage(
    Image.open('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/logout-white.png'))
    logout_btn = Button(sub_header, bg='#304562', image=icon_logout, relief=FLAT,command= log_out)
    logout_btn.grid(row=0, column=3, padx=100, ipady=12)

    # Creating frame for calculator section

    # Creating main frame for calculator
    calcFrame = LabelFrame(frame, bg='#091b33', borderwidth=0, padx=27, pady=15)
    calcFrame.grid(row=1, column=0, sticky=NE, padx=210, pady=200)

    # Creating input field
    inputField = Entry(calcFrame, width=55, bg="#fbfbfb", font=('Code New Roman', 14))
    inputField.focus()
    inputField.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=20, ipady=17)

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
        num_first = int(first_number)
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
        num_first = int(first_number)
        inputField.delete(0, END)

    # To multiply
    def button_multiply():
        first_number = inputField.get()
        global num_first
        global calculation
        calculation = 'multiplication'
        num_first = int(first_number)
        inputField.delete(0, END)

    # To divide
    def button_divide():
        first_number = inputField.get()
        global num_first
        global calculation
        calculation = 'division'
        num_first = int(first_number)
        inputField.delete(0, END)

    # # Creating numeric buttons
    button_0 = Button(calcFrame, text="0", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(0))
    button_1 = Button(calcFrame, text="1", padx=43, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(1))
    button_2 = Button(calcFrame, text="2", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(2))
    button_3 = Button(calcFrame, text="3", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(3))
    button_4 = Button(calcFrame, text="4", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(4))
    button_5 = Button(calcFrame, text="5", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(5))
    button_6 = Button(calcFrame, text="6", padx=45, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(6))
    button_7 = Button(calcFrame, text="7", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(7))
    button_8 = Button(calcFrame, text="8", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(8))
    button_9 = Button(calcFrame, text="9", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                      font=('Code New Roman', 15), command=lambda: click_button(9))

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
    button_add = Button(calcFrame, text="➕", padx=32, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                        font=('Code New Roman', 15,), command=button_add)
    button_sub = Button(calcFrame, text="−", padx=41, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                        font=('Code New Roman', 15,), command=button_subtract)
    button_mul = Button(calcFrame, text="x", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                        font=('Code New Roman', 15,), command=button_multiply)
    button_div = Button(calcFrame, text="÷", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                        font=('Code New Roman', 15,), command=button_divide)
    button_equal = Button(calcFrame, text="=", padx=163, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                          font=('Code New Roman', 15,), command=button_equal)

    # Putting calculation buttons on screen
    button_add.grid(row=1, column=1, padx=5, pady=5)
    button_sub.grid(row=1, column=2, padx=5, pady=5)
    button_mul.grid(row=4, column=0, padx=0, pady=5)
    button_div.grid(row=4, column=1, padx=9, pady=5)
    button_equal.grid(row=4, column=2, columnspan=3, padx=5, pady=5)

    # Creating special buttons
    button_clear = Button(calcFrame, text="C", padx=40, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                          font=('Code New Roman', 15, "bold"), command=clear_button)
    button_off = Button(calcFrame, text="Off", padx=90, pady=20, bg="#304562", fg="#f0ece2", relief=FLAT,
                        font=('Code New Roman', 15,), command=power_off, stat=DISABLED)

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


# ------------------------------------------ END of  Database for registration ---------------------------------------#

# ------------------------------------------------- Signup Page -------------------------------------------------------#

def signup():
    global firstname_entry
    global lastname_entry
    global email_entry
    global username_entry
    global password_entry

    signup_setup = Toplevel()
    signup_setup.geometry('1920x1080')
    signup_setup.title(' Store Management System - Signup')
    signup_setup['background'] = '#304562'

    signup_setup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

    loginBox = LabelFrame(signup_setup, borderwidth=0, bg="#091b33", height=900, width=500, )
    loginBox.grid(row=0, column=0, padx=500, pady=30)

    firstname_label = Label(loginBox, text='First Name', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",
                            font=('Code New Roman', 21))
    firstname_entry = Entry(loginBox, font=('helvetica', 14))
    firstname_entry.focus()
    firstname_label.grid(row=0, column=0, padx=100, pady=10)
    firstname_entry.grid(row=1, column=0, ipadx=50, ipady=10)

    lastname_label = Label(loginBox, text='Last Name', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",
                           font=('Code New Roman', 21))
    lastname_entry = Entry(loginBox, font=('helvetica', 14))
    lastname_label.grid(row=2, column=0, padx=100, pady=10)
    lastname_entry.grid(row=3, column=0, ipadx=50, ipady=10)

    email_label = Label(loginBox, text='Email', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",
                        font=('Code New Roman', 21))
    email_entry = Entry(loginBox, font=('helvetica', 14))
    email_label.grid(row=4, column=0, padx=100, pady=10)
    email_entry.grid(row=5, column=0, ipadx=50, ipady=10)

    username_label = Label(loginBox, text='Username', bg="#091b33", padx=60, pady=15, fg="#f7f7f7",
                           font=('Code New Roman', 21))
    username_entry = Entry(loginBox, font=('helvetica', 14))
    username_label.grid(row=6, column=0, padx=100, pady=10)
    username_entry.grid(row=7, column=0, ipadx=50, ipady=10)

    password_label = Label(loginBox, text="Password", bg="#091b33", padx=60, pady=15, fg="#f7f7f7",
                           font=('Code New Roman', 21))
    password_entry = Entry(loginBox, show='*', font=('helvetica', 14))
    password_label.grid(row=8, column=0, padx=100, pady=10)
    password_entry.grid(row=9, column=0, ipadx=50, ipady=10)

    sub_btn = Button(loginBox, text='Sign Up', bg="#06e6b0", fg="#091b33", font=('Code New Roman', 21),
                     command=register)
    sub_btn.grid(row=10, column=0, pady=25, ipadx=40, ipady=7)


#  -------------------------------------------- END of Signup Page ----------------------------------------------------#

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

            dashboard()

        else:
            messagebox.showerror("Error", "Invalid Username and Password")

    main_database.commit()
    main_database.close()



# --------------------------------------------- Login Page ----------------------------------------------------------#

def home_login():
    global name_entry
    global passw_entry
    login_setup = Toplevel()
    login_setup.geometry('1920x1080')
    login_setup.title('Login')
    login_setup['background'] = '#304562'

    login_setup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

    loginBox = LabelFrame(login_setup, borderwidth=0, bg="#091b33", height=500, width=500, )
    loginBox.grid(row=0, column=0, padx=500, pady=150)

    name_label = Label(loginBox, text='Username', bg="#091b33", padx=60, pady=20, fg="#f7f7f7",
                       font=('Code New Roman', 21))
    name_entry = Entry(loginBox, font=('helvetica', 14))
    name_entry.focus()
    name_label.grid(row=0, column=0, padx=100, pady=10)
    name_entry.grid(row=1, column=0, ipadx=50, ipady=10)

    passw_label = Label(loginBox, text="Password", bg="#091b33", padx=60, pady=20, fg="#f7f7f7",
                        font=('Code New Roman', 21))
    passw_entry = Entry(loginBox, show='*', font=('helvetica', 14))
    passw_label.grid(row=2, column=0, padx=100, pady=10)
    passw_entry.grid(row=3, column=0, ipadx=50, ipady=10)

    login_btn = Button(loginBox, text=' Login ', bg="#06e6b0", fg="#091b33", font=('Code New Roman', 21), command=login)
    login_btn.grid(row=4, column=0, pady=25, ipadx=50, ipady=4)

    register_btn = Button(loginBox, text='Register', bg="#06e6b0", fg="#091b33", font=('Code New Roman', 21),
                          command=signup)
    register_btn.grid(row=5, column=0, pady=25, ipadx=40, ipady=4)

    login_setup.mainloop()

    login_setup.destroy()



# -------------------------------------------------- Show Data -----------------------------------------------------#

def show_total():
    root = Toplevel()
    root.geometry('1920x1080')
    root.title('Store Management System - Total')
    root['background'] = '#304562'
    root.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')

    # Creating frame for tree view
    tree_frame = Frame(root, bg='#304562')
    tree_frame.pack(pady=7, padx=5)


    back_home_btn = Button(tree_frame, bg='#304562', text='❮', relief=FLAT, fg='#f7f7f7', padx=20,
                           font=('HandVetica', 21), command=lambda: root.destroy())
    back_home_btn.place(x=30)

    title = Label(tree_frame, text="Store Management System", bg='#304562', fg='#f7f7f7', font=('HandVetica', 37))
    title.pack(side=TOP,padx=80)

    # Creating clock
    def clock():
        hour = time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000, clock)

    # Displaying time
    show_time = Label(tree_frame, bg='#304562', fg='#f7f7f7', text="", font=('digital-7', 22), padx=50)
    show_time.place(x=1200,y=20)
    clock()

    # Adding style
    style = ttk.Style()

    # Choosing theme  equilux bg='#091b33'
    style.theme_use('classic')

    # Configure the tree color
    style.configure("Treeview",
                    background='#091b33',
                    foreground='black',
                    rowheight=40,
                    fieldbackground='#091b33')

    # Configure Font name and Size
    style.configure("Treeview", font=('Code New Roman', 13))
    style.configure("Treeview.Heading", font=('Code New Roman', 15))

    # Change selected color
    style.map('Treeview',
              background=[('selected', '#06e6b0')])



    # Creating a Tree view Scrollbar Vertical

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Creating a Tree view Scrollbar Horizontal

    tree_scroll_horizontal = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll_horizontal.pack(side=BOTTOM, fill=X)

    # Create the Tree view
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended',
                           xscrollcommand=tree_scroll_horizontal.set)
    my_tree.pack(pady=40)

    # configure scrollbar
    tree_scroll.config(command=my_tree.yview)
    tree_scroll_horizontal.config(command=my_tree.xview)

    # Data from database
    # ------------------------------------------------------------------------------------------------
    # connecting database to tree view
    def connect():
        main_database = sqlite3.connect("storemanagement.db")

        cursor = main_database.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS showdata (billno INTEGER PRIMARY KEY, productname TEXT, productquantity TEXT, productrate TEXT, totalprice TEXT, companyname TEXT, address TEXT, contactnumber TEXT, email TEXT, date TEXT, productdescription TEXT)")

        main_database.commit()
        main_database.close()

    # Showing data at tree view from database
    def View():
        main_database = sqlite3.connect("storemanagement.db")

        cursor = main_database.cursor()

        cursor.execute("SELECT * FROM data_storage")

        rows = cursor.fetchall()

        count = 0

        # To loop through database data
        for row in rows:
            if count % 2 == 0:
                my_tree.insert("", END, values=row, tags=('evenrow',))
            else:
                my_tree.insert("", END, values=row, tags=('oddrow',))
            count += 1

        main_database.close()




    # Define column

    my_tree['columns'] = (
    'Bill No', 'Product Name', 'Product Quantity', 'Product Rate', 'Total Price', 'Company Name', 'Address',
    'Contact Number', 'Email Address', 'Date', 'Description')

    # Format column
    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Bill No', anchor=W, width=100)
    my_tree.column('Product Name', anchor=W, width=160)
    my_tree.column('Product Quantity', anchor=CENTER, width=210)
    my_tree.column('Product Rate', anchor=CENTER, width=160)
    my_tree.column('Total Price', anchor=CENTER, width=160)
    my_tree.column('Company Name', anchor=W, width=200)
    my_tree.column('Address', anchor=W, width=160)
    my_tree.column('Contact Number', anchor=W, width=190)
    my_tree.column('Email Address', anchor=W, width=250)
    my_tree.column('Date', anchor=W, width=140)
    my_tree.column('Description', anchor=W, width=400)

    # Create Heading
    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Bill No', text='Bill No', anchor=W)
    my_tree.heading('Product Name', text='Product Name', anchor=W)
    my_tree.heading('Product Quantity', text='Product Quantity', anchor=CENTER)
    my_tree.heading('Product Rate', text='Product Rate', anchor=CENTER)
    my_tree.heading('Total Price', text='Total Price', anchor=CENTER)
    my_tree.heading('Company Name', text='Company Name', anchor=CENTER)
    my_tree.heading('Address', text='Address', anchor=CENTER)
    my_tree.heading('Contact Number', text='Contact Number', anchor=CENTER)
    my_tree.heading('Email Address', text='Email Address', anchor=CENTER)
    my_tree.heading('Date', text='Date', anchor=CENTER)
    my_tree.heading('Description', text='Description', anchor=CENTER)

    # Create Striped Row Tag

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='#fcf1f1')

    # Button to show data

    button1 = Button(tree_frame, text="View data", bg="#06e6b0",padx=20,pady=20, fg="#091b33", font=('Code New Roman', 21),
                     command=View)
    button1.pack(pady=60)


#------------------------------------------------  End of Show Data -------------------------------------------------#

# -----------------------------------------------------For Login dashboard ------------------------------------------#
global name_entry
global passw_entry
login_setup = Tk()
login_setup.geometry('1920x1080')
login_setup.title('Login')
login_setup['background'] = '#304562'

login_setup.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

loginBox = LabelFrame(login_setup, borderwidth=0, bg="#091b33", height=500, width=500, )
loginBox.grid(row=0, column=0, padx=500, pady=150)

name_label = Label(loginBox, text='Username', bg="#091b33", padx=60, pady=20, fg="#f7f7f7", font=('Code New Roman', 21))
name_entry = Entry(loginBox, font=('helvetica', 14))
name_entry.focus()
name_label.grid(row=0, column=0, padx=100, pady=10)
name_entry.grid(row=1, column=0, ipadx=50, ipady=10)

passw_label = Label(loginBox, text="Password", bg="#091b33", padx=60, pady=20, fg="#f7f7f7",font=('Code New Roman', 21))
passw_entry = Entry(loginBox, show='*', font=('helvetica', 14))
passw_label.grid(row=2, column=0, padx=100, pady=10)
passw_entry.grid(row=3, column=0, ipadx=50, ipady=10)

login_btn = Button(loginBox, text=' Login ', bg="#06e6b0", fg="#091b33", font=('Code New Roman', 21), command=login)
login_btn.grid(row=4, column=0, pady=25, ipadx=50, ipady=4)

register_btn = Button(loginBox, text='Register', bg="#06e6b0", fg="#091b33", font=('Code New Roman', 21),command=signup)
register_btn.grid(row=5, column=0, pady=25, ipadx=40, ipady=4)

login_setup.mainloop()
