import tkinter 
from tkinter import * 
import pymysql
from dashboardofcompanymaster import *
from dashboardofdepartment import *
from dashboardofemployee import *
from dashboardofempsalary import *
from dashboardofhodtable import *
from dashboardofholidaymaster import *
from dashboardofpayment import *

def showmaindashboard():

    t=tkinter.Tk()
    t.geometry('600x600')

    d=Canvas(t,width=600,height=600)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,580,580,fill='black')
    d.create_rectangle(25,25,575,575,fill='#ADD8E6')
    t.title('Main')
    
    def cts():
        t.destroy()
    
    a=Label(t,text='Main Dashboard',font=('arial',15),bg='#ADD8E6')
    a.place(x=200,y=40)
    
    bt=Button(t,text='Company Master',command=showdashboardofcompanymaster)
    bt.place(x=50,y=100)
    
    bt=Button(t,text='Department',command=showdashboardofdepartment)
    bt.place(x=200,y=100)
    
    bt=Button(t,text='HOD Table',command=showdashboardofhodtable)
    bt.place(x=350,y=100)
    
    bt=Button(t,text='Employee',command=showdashboardofemployee)
    bt.place(x=50,y=180)
    
    bt=Button(t,text='Employee Salary',command=showdashboardofempsalary)
    bt.place(x=200,y=180)
    
    bt=Button(t,text='Holiday Master',command=showdashboardofholidaymaster)
    bt.place(x=350,y=180)
    
    bt=Button(t,text='Payment',command=showdashboardofpayment)
    bt.place(x=200,y=260)
    
    bt=Button(t,text='CLOSE',font=('arial',10),command=cts)
    bt.place(x=200,y=330)
    
    t.mainloop()