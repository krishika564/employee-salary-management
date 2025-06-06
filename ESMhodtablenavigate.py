import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMhodtablenavigate():
    
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
    i=0
     
    def first():
        global i
        i=0 
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
         
    def second():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
         
    def last():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        sql="select HODid,HODname,deptid,remarks from HODTable"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(str(res[2]))
            xd.append(res[3])
        db.close()
    
    b1=Label(t,text="Employee Salary Management",fg='darkblue',font=('arial',10),bg='#FFEDD1')
    b1.place(x=300,y=40)
    b2=Label(t,text='HODTable',bg='#FFEDD1')
    b2.place(x=350,y=70)
    
    a1=Label(t,text='HODID',bg='#FFEDD1')
    a1.place(x=100,y=110)
    e1=Entry(t,width=30)
    e1.place(x=400,y=110)
    
    a2=Label(t,text='HOD Name',bg='#FFEDD1')
    a2.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    a3=Label(t,text='Department ID',bg='#FFEDD1')
    a3.place(x=100,y=190)
    e3=Entry(t,width=30)
    e3.place(x=400,y=190)
    
    a4=Label(t,text='Remarks',bg='#FFEDD1')
    a4.place(x=100,y=230)
    e4=Entry(t,width=30)
    e4.place(x=400,y=230)
    
    bt1=Button(t,text='First',command=first,bg='#C0C0C0')
    bt1.place(x=100,y=320)
    
    bt2=Button(t,text='Next',command=second,bg='#C0C0C0')
    bt2.place(x=200,y=320)
    
    bt3=Button(t,text='Last',command=last,bg='#C0C0C0')
    bt3.place(x=300,y=320)
    
    bt4=Button(t,text='Previous',command=pt,bg='#C0C0C0')
    bt4.place(x=400,y=320)
    
    filldata()
    t.mainloop()