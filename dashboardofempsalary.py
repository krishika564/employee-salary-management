import tkinter 
from tkinter import * 
import pymysql 
from tkinter import messagebox
from ESMempsalarydelete import *
from ESMempsalaryfind import *
from ESMempsalarynavigate import *
from ESMempsalarysave import *
from ESMempsalaryshow import *
from ESMempsalaryupdate import *

def showdashboardofempsalary():
    
    t=tkinter.Tk()
    t.geometry('600x600')

    d=Canvas(t,width=600,height=600)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,580,580,fill='black')
    d.create_rectangle(25,25,575,575,fill='#CBC3E3')
    
    a=Label(t,text='DashBoard of Employee Salary',fg='black',font=('arial',20),bg='#CBC3E3')
    a.place(x=180,y=50)
    
    bt1=Button(t,text='Save',command=showESMempsalarysave)
    bt1.place(x=100,y=100)
    
    bt2=Button(t,text='Find',command=showESMempsalaryfind)
    bt2.place(x=100,y=140)
    
    bt3=Button(t,text='Delete',command=showESMempsalarydelete)
    bt3.place(x=100,y=180)
    
    bt4=Button(t,text='Update',command=showESMempsalaryupdate)
    bt4.place(x=100,y=220)
    
    bt5=Button(t,text='Show',command=showESMempsalaryshow)
    bt5.place(x=100,y=260)
    
    bt6=Button(t,text='Navigate',command=showESMempsalarynavigate)
    bt6.place(x=100,y=300)
    
    t.mainloop()