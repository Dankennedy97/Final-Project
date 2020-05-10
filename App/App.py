from tkinter import *
import os

#Youtube video 1 https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=578s
#Youtube video 2 https://www.youtube.com/watch?v=Z-deSpgtIG0&t=20s
#Youtube video 3 https://www.youtube.com/watch?v=OqfcGng4oKs

def delete2():
    screen4.destroy()

def delete():
    screen3.destroy()

#def logoff():
    # screen7.destroy()

def saved():
    screen7 = Toplevel(screen)
    screen7.title("Saved")
    screen7.geometry("100x100")
    Label(screen7, text = "Saved").pack()

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

    screen6 = Toplevel(screen)
    screen6.title("Adding a Password")
    screen6.geometry("300x250")
    Label(screen6, text = "Please enter your username : ").pack()
    Entry(screen6, textvariable = raw_user).pack()
    Label(screen6, text = "Please enter your password : ").pack()
    Entry(screen6, textvariable = raw_pass).pack()
    #radio_button = Radiobutton(screen6, variable = v, value = 0, text = "Just Add Password", command = lambda: print(v.get())).pack()
    #radio_button2 = Radiobutton(screen6, variable = v, value = 1, text= "Add Password and Corresponding Account", command = lambda: print(v.get())).pack()
    #radio_button3 = Radiobutton(screen6, variable = v, value = 2, text= "Generate a Strong Random Password",  command = lambda: print(v.get())).pack()
    Button(screen6, text = "Save", command = save).pack()


def session():
    screen5 = Toplevel(screen)
    screen5.title("Dashboard")
    screen5.geometry("400x400")
    Label(screen5, text = "Welcome the the Dashboard of the Password Manager").pack()
    Button(screen5, text = "Add Password", command = add_pass).pack()
    Button(screen5, text = "Manage Existing Passwords").pack()
    Button(screen5, text = "Settings").pack()

def login_success():
    session()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password does not exist").pack()
    Button(screen4, text="OK", command=delete2).pack()

def user_not_found():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="User does not exist").pack()
    Button(screen3, text="OK", command=delete).pack()

def reg_user():
    username_info = username.get()
    password_info = password.get()
    password_info_1 = conf_pass.get()

    if password_info == password_info_1:
        file = open(username_info, "w")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()
        Label(screen1, text="Reg Success", fg="green", font=("calibri", 11)).pack()
    else:
        Label(screen1, text="Reg Fail, Passwords did not match", fg="green", font=("calibri", 11)).pack()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    conf_pass_entry.delete(0, END)

def log_verify():
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
    global conf_pass
    global username_entry
    global password_entry
    global conf_pass_entry
    username = StringVar()
    password = StringVar()
    conf_pass = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="Confirm Password * ").pack()
    conf_pass_entry = Entry(screen1, textvariable = conf_pass)
    conf_pass_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = reg_user).pack()

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
    Button(screen2, text = "Login", width = 10, height = 1, command = log_verify).pack()

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
