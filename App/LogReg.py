from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('C:\Users\Dank\Desktop\Final-Project\Database-Key\splitpass-51856c900d2f.json')
firebase_admin.initialize_app(cred, {
    'https://splitpass-6dab1.firebaseio.com/'
})

ref = db.reference('restricted_access/secret_document')
print(ref.get())

GUI = Tk()

def delete():
    screen.destroy()

def delete2():
    screen1.destroy()

def regUser(firebase=None):

    
    data = {
        'First Name': fName,
        'Surname': lName,
        'User': username,
        'Email': email,
        'Password': password,
    }
    result = firebase.post('/splitpass-6dab1/Users', data)
    print(result)

    fNameE.delete(0, END)
    lNameE.delete(0, END)
    userE.delete(0, END)
    emailE.delete(0, END)
    passE.delete(0, END)
    confPassE.delete(0, END)

    Label(screen1, text = "Reg Success", fg = "green", font = ("calibri", 11)).pack()

def reg():
    global screen1
    screen1 = Toplevel(GUI)
    screen1.title("Registration")
    screen1.geometry("1000x700")
    global fName
    global lName
    global username
    global email
    global password
    global fNameE
    global lNameE
    global userE
    global emailE
    global passE
    global confPassE
    fName = StringVar()
    lName = StringVar()
    username = StringVar()
    email = StringVar()
    password = StringVar()
    confPass = StringVar()

    Label(screen1, text = "Please enter your details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "First Name").pack()
    fNameE = Entry(screen1, textvariable = fName)
    fNameE.pack()
    Label(screen1, text = "Last Name").pack()
    lNameE = Entry(screen1, textvariable = lName)
    lNameE.pack()
    Label(screen1, text = "Username ").pack()
    userE = Entry(screen1, textvariable = username)
    userE.pack()
    Label(screen1, text = "Email ").pack()
    userE = Entry(screen1, textvariable = email)
    userE.pack()
    Label(screen1, text = "Password ").pack()
    passE = Entry(screen1, textvariable = password)
    passE.pack()
    Label(screen1, text = " Confirm Password ").pack()
    passE = Entry(screen1, textvariable = confPass)
    passE.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = regUser()).pack()

def login():
    global screen
    screen = Toplevel(GUI)
    screen.title("Login")
    screen.geometry("1000x700")
    Label(screen, text = "Please enter details below to Login").pack()
    Label(screen, text = "").pack

    global userV
    global passV
    userV = StringVar()
    passV = StringVar()

    global userE1
    global passE1
    Label(screen, text = "Username here").pack()
    userE1 = Entry(screen, textvariable = userV)
    userE1.pack()
    Label(screen, text = "Password Here").pack()
    passE1 = Entry(screen, textvariable = passV)
    passE1.pack()
    Label(screen, text = "").pack()
    Button(screen, text = "Login", width = 10, height = 1).pack()


GUI.title("Password Manager")
GUI.geometry("300x250")
Label(text = "SplitPass Manger", bg = "black", width = "1000", height = "2", font = ("Calibri", 13)).pack()
Label(text = "").pack()
Button(text="Login", height="2", width="30", command = login).pack()
Label(text="").pack()
Button(text="Register", height="2", width="30", command = reg).pack()

GUI.mainloop()