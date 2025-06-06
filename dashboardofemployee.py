
import tkinter 
from tkinter import * 
import pymysql 
from tkinter import messagebox
from ESMemployeedelete import *
from ESMemployeefind import *
from ESMemployeenavigate import *
from ESMemployeesave import *
from ESMemployeeshow import *
from ESMemployeeupdate import *

def showdashboardofemployee():
    
    t=tkinter.Tk()
    t.geometry('600x600')

    d=Canvas(t,width=600,height=600)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,580,580,fill='black')
    d.create_rectangle(25,25,575,575,fill='#CBC3E3')
    
    a=Label(t,text='DashBoard of Employee',fg='black',font=('arial',20),bg='#CBC3E3')
    a.place(x=250,y=50)
    
    bt1=Button(t,text='Save',command=showESMemployeesave)
    bt1.place(x=100,y=100)
    
    bt2=Button(t,text='Find',command=showESMemployeefind)
    bt2.place(x=100,y=140)
    
    bt3=Button(t,text='Delete',command=showESMemployeedelete)
    bt3.place(x=100,y=180)
    
    bt4=Button(t,text='Update',command=showESMemployeeupdate)
    bt4.place(x=100,y=220)
    
    bt5=Button(t,text='Show',command=showESMemployeeshow)
    bt5.place(x=100,y=260)
    
    bt6=Button(t,text='Navigate',command=showESMemployeenavigate)
    bt6.place(x=100,y=300)
    
    t.mainloop()