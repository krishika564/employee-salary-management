import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMpaymentfind():
    
    t=tkinter.Tk()
    t.geometry('700x700')
    
    d=Canvas(t,width=700,height=700)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,680,680,fill='black')
    d.create_rectangle(25,25,675,675,fill='#FFEDD1')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select empid from employee"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1['values']=lt
        
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select month, deptid, noofleaves, payment, tax, netpay from Payment where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,data[5])
        db.close()
        
    def payment():
        xa=int(e2.get())
        xb=int(e4.get())
        dt=xa/30
        net=round((31-xb)*dt)
        e5.delete(0,100)
        e5.insert(0,str(net))
        
    def tax():
        rt=int(e5.get())
        tx=rt*0.10
        e6.delete(0,100)
        e6.insert(0,str(round(tx)))
        
    def netpay():
        xa=int(e5.get())
        xb=int(e6.get())
        xd=xa-xb
        e7.delete(0,100)
        e7.insert(0,str(round(xd)))
            
    def close():
        t.destroy()
        
    b1=Label(t,text="Employee Salary Management",fg='darkblue',font=('arial',10),bg='#FFEDD1')
    b1.place(x=300,y=40)
    b2=Label(t,text='Payment of Employees',bg='#FFEDD1')
    b2.place(x=350,y=70)
    
    a1=Label(t,text='Employee ID',bg='#FFEDD1')
    a1.place(x=100,y=110)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=400,y=110)
    
    a2=Label(t,text='Month',bg='#FFEDD1')
    a2.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    a3=Label(t,text='Department ID',bg='#FFEDD1')
    a3.place(x=100,y=190)
    e3=Entry(t,width=30)
    e3.place(x=400,y=190)
    
    a4=Label(t,text='Number of Leaves',bg='#FFEDD1')
    a4.place(x=100,y=230)
    e4=Entry(t,width=30)
    e4.place(x=400,y=230)
    
    a5=Button(t,text='Payment',command=payment,bg='#C0C0C0')
    a5.place(x=100,y=270)
    e5=Entry(t,width=30)
    e5.place(x=400,y=270)
    
    a6=Button(t,text='Tax',command=tax,bg='#C0C0C0')
    a6.place(x=100,y=310)
    e6=Entry(t,width=30)
    e6.place(x=400,y=310)
    
    a7=Button(t,text='Netpay',command=netpay,bg='#C0C0C0')
    a7.place(x=100,y=350)
    e7=Entry(t,width=30)
    e7.place(x=400,y=350)
    
    bt=Button(t,text='FIND',command=finddata,bg='#C0C0C0')
    bt.place(x=250,y=390)
    
    bt=Button(t,text='Close',command=close,bg='#C0C0C0')
    bt.place(x=350,y=390)
    
    t.mainloop()
    
#showESMpaymentfind()