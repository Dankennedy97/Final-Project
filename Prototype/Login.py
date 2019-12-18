from tkinter import *
import os

#def delete2():
    # screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

#def logoff():
    # screen7.destroy()

def saved():
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("100x100")
    Label(screen10, text = "Saved").pack()

def save():
    filename = raw_user.get()
    password = raw_pass.get()

    data = open(filename, "w")
    data.write(password)
    data.close()

    saved()

def add_pass():
    global raw_user
    raw_user = StringVar()
    global raw_pass
    raw_pass = StringVar()

    screen9 = Toplevel(screen)
    screen9.title("Adding a Password")
    screen9.geometry("300x250")
    Label(screen9, text = "Please enter your username : ").pack()
    Entry(screen9, textvariable = raw_user).pack()
    Label(screen9, text = "Please enter your password : ").pack()
    Entry(screen9, textvariable = raw_pass).pack()
    #radio_button = Radiobutton(screen9, variable = v, value = 0, text = "Just Add Password", command = lambda: print(v.get())).pack()
    #radio_button2 = Radiobutton(screen9, variable = v, value = 1, text= "Add Password and Corresponding Account", command = lambda: print(v.get())).pack()
    #radio_button3 = Radiobutton(screen9, variable = v, value = 2, text= "Generate a Strong Random Password",  command = lambda: print(v.get())).pack()
    Button(screen9, text = "Save", command = save).pack()


def session():
    screen8 = Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome the the Dashboard of the Password Manager").pack()
    Button(screen8, text = "Add Password", command = add_pass).pack()
    Button(screen8, text = "Manage Existing Passwords").pack()
    Button(screen8, text = "Settings").pack()

def login_success():
    session()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password does not exist").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User does not exist").pack()
    Button(screen5, text="OK", command=delete4).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Reg Success", fg = "green", font = ("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()

    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    global Tk
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Password Manager")
    Label(text = "Password Manager", bg="grey", width="300", height="2", font=("Arial", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height="2", width="30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height="2", width="30", command = register).pack()

    screen.mainloop()

main_screen()
