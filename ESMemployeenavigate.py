import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMemployeenavigate():
    
    t=tkinter.Tk()
    t.geometry('700x700')
    
    d=Canvas(t,width=700,height=700)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,680,680,fill='black')
    d.create_rectangle(25,25,675,675,fill='#FFEDD1')
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    i=0
     
    def first():
        global i
        i=0 
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
         
    def second():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
         
    def last():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        sql="select empid,name,address,city,email,phone,deptid from Employee"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            xf.append(str(res[5]))
            xg.append(str(res[6]))
        db.close()
    
    b1=Label(t,text="Employee Salary Management",fg='darkblue',font=('arial',10),bg='#FFEDD1')
    b1.place(x=300,y=40)
    b2=Label(t,text='Employee',bg='#FFEDD1')
    b2.place(x=350,y=70)
    
    a1=Label(t,text='Employee ID',bg='#FFEDD1')
    a1.place(x=100,y=110)
    e1=Entry(t,width=30)
    e1.place(x=400,y=110)
    
    a2=Label(t,text='Name',bg='#FFEDD1')
    a2.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    a3=Label(t,text='Address',bg='#FFEDD1')
    a3.place(x=100,y=190)
    e3=Entry(t,width=30)
    e3.place(x=400,y=190)
    
    a4=Label(t,text='City',bg='#FFEDD1')
    a4.place(x=100,y=230)
    e4=Entry(t,width=30)
    e4.place(x=400,y=230)
    
    a5=Label(t,text='Email',bg='#FFEDD1')
    a5.place(x=100,y=270)
    e5=Entry(t,width=30)
    e5.place(x=400,y=270)
    
    a6=Label(t,text='Phone',bg='#FFEDD1')
    a6.place(x=100,y=310)
    e6=Entry(t,width=30)
    e6.place(x=400,y=310)
    
    a7=Label(t,text='Department ID',bg='#FFEDD1')
    a7.place(x=100,y=350)
    e7=Entry(t,width=30)
    e7.place(x=400,y=350)
    
    bt1=Button(t,text='First',command=first,bg='#C0C0C0')
    bt1.place(x=100,y=390)
    
    bt2=Button(t,text='Next',command=second,bg='#C0C0C0')
    bt2.place(x=200,y=390)
    
    bt3=Button(t,text='Last',command=last,bg='#C0C0C0')
    bt3.place(x=300,y=390)
    
    bt4=Button(t,text='Previous',command=pt,bg='#C0C0C0')
    bt4.place(x=400,y=390)
    
    filldata()
    t.mainloop()