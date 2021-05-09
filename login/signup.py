from tkinter import *
# from PIL import ImageTk, Image
root = Tk()

root.geometry('1920x1080')
root.title(' Store Management System - Signup')
root['background'] = '#304562'

root.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

loginBox = LabelFrame(root,borderwidth=0, bg="#091b33",height=900,width=500,)
loginBox.grid(row=0,column=0,padx=500,pady=30)

name_var = StringVar()
passw_var = StringVar()

name_var.set("")
passw_var.set("")


def submit():
    name = name_var.get()
    password = passw_var.get()

    print(f"The username is {name}")
    print(f"The Password is {password}")


firstname_label = Label(loginBox, text='First Name',bg="#091b33",padx=60,pady=15,fg="#f7f7f7", font=('Code New Roman',21))
firstname_entry = Entry(loginBox, textvariable=name_var, font=('helvetica', 14))
firstname_label.grid(row=0, column=0, padx=100, pady=10)
firstname_entry.grid(row=1, column=0, ipadx=50, ipady=10)


lastname_label = Label(loginBox, text='Last Name',bg="#091b33",padx=60,pady=15,fg="#f7f7f7", font=('Code New Roman',21))
lastname_entry = Entry(loginBox, textvariable=name_var, font=('helvetica', 14))
lastname_label.grid(row=2, column=0, padx=100, pady=10)
lastname_entry.grid(row=3, column=0, ipadx=50, ipady=10)


email_label = Label(loginBox, text='Email',bg="#091b33",padx=60,pady=15,fg="#f7f7f7", font=('Code New Roman',21))
email_entry = Entry(loginBox, textvariable=name_var, font=('helvetica', 14))
email_label.grid(row=4, column=0, padx=100, pady=10)
email_entry.grid(row=5, column=0, ipadx=50, ipady=10)


username_label = Label(loginBox, text='Username',bg="#091b33",padx=60,pady=15,fg="#f7f7f7", font=('Code New Roman',21))
username_entry = Entry(loginBox, textvariable=name_var, font=('helvetica', 14))
username_label.grid(row=6, column=0, padx=100, pady=10)
username_entry.grid(row=7, column=0, ipadx=50, ipady=10)


password_label = Label(loginBox, text="Password",bg="#091b33",padx=60,pady=15,fg="#f7f7f7", font=('Code New Roman', 21))
password_entry = Entry(loginBox, textvariable=passw_var, show='*', font=('helvetica', 14))
password_label.grid(row=8, column=0, padx=100, pady=10)
password_entry.grid(row=9, column=0, ipadx=50, ipady=10)


sub_btn = Button(loginBox, text='Sign Up' ,bg="#06e6b0",fg="#091b33",command=submit, font=('Code New Roman', 21))
sub_btn.grid(row=10, column=0,pady=25, ipadx=40, ipady=7)


root.mainloop()