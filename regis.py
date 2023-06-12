from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"

root = Tk()
root.title("New User Registration")  ## Window Title
root.geometry("1250x700+210+100")    ## window size
root.config(bg=background)
root.resizable(False, False)

def register():
    username = user.get()
    password = code.get()
    admincode = adminacess.get()

    print(username, password, admincode)
    if admincode == "9955":
        if (username == "" or username == "userid") or (password == "" or password == "Password"):
            messagebox.showerror("Entry error!", "Type Username or Password !!! ")
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user='root', password='Rashed2450')
                mycursor = mydb.cursor()
                print("Connection Stabilized !!!")
            except:
                messagebox.showerror("Connection", "Database connection not stabilized !!!")

            try:
                mycursor.execute("CREATE DATABASE IF NOT EXISTS StudentRegistration")
                mycursor.execute("USE StudentRegistration")
                mycursor.execute("CREATE TABLE IF NOT EXISTS login (user INT AUTO_INCREMENT PRIMARY KEY, "
                                 "Username VARCHAR(50), Password VARCHAR(100))")
            except Exception as e:
                print("Error:", e)
                messagebox.showerror("Error", "An error occurred while creating the table.")
                return

            try:
                command = "INSERT INTO login(Username, Password) VALUES (%s, %s)"
                values = (username, password)
                mycursor.execute(command, values)
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register", "New User Added Successfully!!!")
            except Exception as e:
                print("Error:", e)
                messagebox.showerror("Error", "An error occurred while inserting data into the table.")
                return

    else:
        messagebox.showerror("Admin code!", "Input Correct Admin Code to Add New User")

def login():
    root.destroy()

# icon image
image_icon = PhotoImage(file="C:\\Users\\admin\\Downloads\\sm vita\\python\\classpython\\pythonpr1\\login.png")
root.iconphoto(False, image_icon)

# background image
frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="C:\\Users\\admin\\Downloads\\sm vita\\python\\classpython\\pythonpr1\\new2.png")
Label(frame, image=backgroundimage).pack()

adminacess = Entry(root, width=11, fg="#000", border=0, bg="#e8ecf7", font=("Arial Bold", 12), show="*")
adminacess.focus()
adminacess.place(x=567, y=147)

def user_enter(e):
    user.delete(0, 'end')

def user_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "userid")

user = Entry(root, width=11, fg="#fff", bg="#375174", border=0, font=("Arial Bold", 12))
user.insert(0, "Enter userid")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=567, y=172)

def password_enter(e):
    code.delete(0, 'end')

def password_leave(e):
    password = code.get()
    if password == '':
        code.delete(0, 'end')
        code.insert(0, "Password")

code = Entry(root, width=11, fg="#fff", bg="#375174", border=0, font=("Arial Bold", 12))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=567, y=210)

regis_button = Button(root, text="Add New User", bg="#455c88", fg="white", width=11, height=1,
                      font=("Arial", 8, "bold"), bd=0, command=register)
regis_button.place(x=585, y=290)

backbuttonimage = PhotoImage(file="C:\\Users\\admin\\Downloads\\sm vita\\python\\classpython\\pythonpr1\\searchiconnew1.PNG")
Backbutton = Button(root, image=backbuttonimage, fg="#deeefb", command=login)
Backbutton.place(x=20, y=15)

root.mainloop()
