import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMcompanyfind():
    
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
        sql="select compid from CompanyMaster"
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
        sql="select name,address,city,phone,email from CompanyMaster where compid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,int(data[3]))
        e6.insert(0,data[4])
        db.close()
        
    def close():
        t.destroy()
    
    b1=Label(t,text="Employee Salary Management",fg='darkblue',font=('arial',10),bg='#FFEDD1')
    b1.place(x=300,y=40)
    b2=Label(t,text='CompanyMaster',bg='#FFEDD1')
    b2.place(x=350,y=70)
    
    a1=Label(t,text='CompanyID',bg='#FFEDD1')
    a1.place(x=100,y=110)
    e1=ttk.Combobox(d)
    filldata()
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
    
    a5=Label(t,text='Phoneno',bg='#FFEDD1')
    a5.place(x=100,y=270)
    e5=Entry(t,width=30)
    e5.place(x=400,y=270)
    
    a6=Label(t,text='Email',bg='#FFEDD1')
    a6.place(x=100,y=310)
    e6=Entry(t,width=30)
    e6.place(x=400,y=310)
    
    bt=Button(t,text='Find',command=finddata,bg='#C0C0C0')
    bt.place(x=250,y=380)
    
    bt=Button(t,text='Close',command=close,bg='#C0C0C0')
    bt.place(x=350,y=380)
    
    t.mainloop()