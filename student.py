from tkinter import *
from datetime import date
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image , ImageTk
import os 
from tkinter .ttk import Combobox
import openpyxl ,xlrd
from openpyxl import Workbook
import pathlib
import mysql.connector as m

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)






file=pathlib.Path("Student_data.xlsx")
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Class"
    sheet['D1']="Gender"
    sheet['E1']="DOB"
    sheet['F1']="Date of Registration"
    sheet['G1']="Religion"
    sheet['H1']="skill"
    sheet['I1']="Father Name"
    sheet['J1']="Mother Name"
    sheet['K1']="Father's Occupation"
    sheet['L1']="Mothers Occupation"
    #sheet['A1']=""
    
    
    file.save('Student_data.xlsx')
    
    
#### Exit ###  window
def Exit():
    root.destroy()
    
    
############### gender   ###########################################

def selection():
    value=radio.get()
    if value==1:
        gender="Male"
        print(gender)
    else:
        gender="Female"
        print(gender)
    
    
    ########### TOP Frames    ##################
    
label=Label(root,text="Email : sm-vitacdac@gmail.com",width=10,height=3,bg="green",anchor='e').pack(side=TOP,fill=X)
label=Label(root,text="STUDENT REGISTRATON ",width=10,height=2,bg="black",fg='#fff',font='arial 20 bold').pack(side=TOP,fill=X)


#### search box to Update #######################
Search=StringVar()
Entry(root,textvariable=Search,width=10,bd=2,font="arial 20").place(x=920,y=70)
#imageicon3=PhotoImage(file='C:/Users/admin/Downloads/sm vita/python/classpython/pythonpr1/searchicon.jpg')
Srch=Button(root,text="Search",compound=LEFT,width=15,bg='#68ddfa',font='arial 13 bold')
Srch.place(x=1100,y=68)       


update_button=Button(root,bg="#c36464",width=10,text="Update")
update_button.place(x=110,y=64)


########## Registration #### Date

Label(root,text="Registration No:",font="arial 13",fg=framebg,bg=background).place(x=30,y=150)
Label(root,text="Date:",font="arial 13",fg=framebg,bg=background).place(x=500,y=150)

Registration=StringVar()
Date=StringVar()


reg_entry= Entry(root,textvariable=Registration,width=15,font="arial 10")
reg_entry.place(x=160,y=150)


#registration_no()


today=date.today()
d1=today.strftime("%d/%m/%Y")
date_entry= Entry(root,textvariable=Date,width=15,font="arial 10").place(x=550,y=150)

Date.set(d1)



######### Student details

obj=LabelFrame(root,text="Student's Detail",font=20,bd=2,width=900,bg=framebg,fg='black',height=250,relief=GROOVE)
obj.place(x=20,y=200)

Label(obj,text="Full Name:",font="arial 13",bg=framebg,fg='black').place(x=30,y=50)
Label(obj,text="Date of Birth:",font="arial 13",bg=framebg,fg='black').place(x=30,y=100)
Label(obj,text="Gender:",font="arial 13",bg=framebg,fg='black').place(x=30,y=150)


Label(obj,text="Class:",font="arial 13",bg=framebg,fg='black').place(x=500,y=50)
Label(obj,text="Religion:",font="arial 13",bg=framebg,fg='black').place(x=500,y=100)
Label(obj,text="Skills:",font="arial 13",bg=framebg,fg='black').place(x=500,y=150)


Name=StringVar()
name_entry= Entry(obj,textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y=50)


DOB=StringVar()
dob_entry= Entry(obj,textvariable=DOB,width=20,font="arial 10")
dob_entry.place(x=160,y=100)



radio=IntVar()
R1= Radiobutton(obj,text="Male",variable=radio,value=1,bg=framebg,fg='black',command=selection)
R1.place(x=150,y=150)

R2= Radiobutton(obj,text="Female",variable=radio,value=2,bg=framebg,fg='black',command=selection)
R2.place(x=200,y=150)

Religion=StringVar()
religion_entry= Entry(obj,textvariable=Religion,width=20,font="arial 10")
religion_entry.place(x=630,y=100)



Skill=StringVar()
skill_entry= Entry(obj,textvariable=Skill,width=20,font="arial 10")
skill_entry.place(x=630,y=150)


Class=Combobox(obj,values=['1','2','3','4','5','6','7','8','9','10','11','12'],font="Roboto 10",width=17,state="r")
Class.place(x=630,y=50)
Class.set("Select Class")



#####################
############## Paarents Detail#####

obj2=LabelFrame(root,text="Parent's Detail",font=20,bd=2,width=900,bg=framebg,fg='black',height=220,relief=GROOVE)
obj2.place(x=20,y=470)



Label(obj2,text="Father's Name:",font="arial 13",bg=framebg,fg='black').place(x=30,y=50)
Label(obj2,text="Occupation's Name:",font="arial 13",bg=framebg,fg='black').place(x=30,y=100)


F_Name=StringVar()
f_entry=Entry(obj2,textvariable=F_Name,font="arial 10",width=20)
f_entry.place(x=160,y=50)


Father_Occupation=StringVar()
fo_entry=Entry(obj2,textvariable=Father_Occupation,width=20,font="arial 10")
fo_entry.place(x=160,y=100)


##################
Label(obj2,text="Mother's Name:",font="arial 13",bg=framebg,fg='black').place(x=500,y=50)
Label(obj2,text="Occupation's Name:",font="arial 13",bg=framebg,fg='black').place(x=500,y=100)


M_Name=StringVar()
m_entry=Entry(obj2,textvariable=M_Name,font="arial 10",width=20)
m_entry.place(x=630,y=50)


Mother_Occupation=StringVar()
mo_entry=Entry(obj2,textvariable=Mother_Occupation,width=20,font="arial 10")
mo_entry.place(x=630,y=100)


#######image############
f=Frame(root,bd=3,bg="black",width=200,height=200,relief=GROOVE)
f.place(x=1000,y=150)

#img=PhotoImage(file="search-icon.jpg")
lbl=Label(root,bg="black")
lbl.place(x=0,y=0)




##########Button##


Button(root,text="Upload",width=19,height=2,font="arial 12 bold",bg="#E3CF57").place(x=1000,y=370)

### can add imagecommand=showimage

saveButton=Button(root,text="Save",width=19,height=2,font="arial 12 bold",bg="lightgreen")
saveButton.place(x=1000,y=450)

Button(root,text="Reset",width=19,height=2,font="arial 12 bold",bg="lightpink").place(x=1000,y=530)

Button(root,text="Exit",width=19,height=2,font="arial 12 bold",bg="grey",command=Exit).place(x=1000,y=610)









    
    
    
    
    
    
    
    
    
    
root.mainloop()