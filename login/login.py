from tkinter import *
# from PIL import ImageTk, Image
root = Tk()

root.geometry('1920x1080')
root.title('Login')
root['background'] = '#c4c4c4'

root.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/login_key.ico')

loginBox = Frame(root, bg="#8e8b8b")
loginBox.pack(side=TOP, pady=100)

name_var = StringVar()
passw_var = StringVar()

name_var.set("")
passw_var.set("")


def submit():
    name = name_var.get()
    password = passw_var.get()

    print(f"The username is {name}")
    print(f"The Password is {password}")


name_label = Label(loginBox, text='Username', font=('firacode', 14))
name_entry = Entry(loginBox, textvariable=name_var, font=('firacode', 10))

passw_label = Label(loginBox, text="Password", font=('firacode', 14))
passw_entry = Entry(loginBox, textvariable=passw_var, show='*', font=('firacode', 10))

sub_btn = Button(loginBox, text='Submit', command=submit, font=('firacode', 14))

name_label.grid(row=0, column=0, padx=100, pady=10)
name_entry.grid(row=1, column=0, padx=100, pady=10)
passw_label.grid(row=2, column=0, padx=100, pady=10)
passw_entry.grid(row=3, column=0, padx=100, pady=10)
sub_btn.grid(row=4, column=0, padx=100, pady=10)

root.mainloop()