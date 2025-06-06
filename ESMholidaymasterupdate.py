import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMholidaymasterupdate():
    
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
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        sql="update HolidayMaster set holidayname,noofleaves where empid=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('message for you','Data update')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        db.close()
        
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select holidayname,noofleaves from HolidayMaster where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
            
    def close():
        t.destroy()
    
    b1=Label(t,text="Employee Salary Management",fg='darkblue',font=('arial',10),bg='#FFEDD1')
    b1.place(x=300,y=40)
    b2=Label(t,text='Holiday Master',bg='#FFEDD1')
    b2.place(x=350,y=70)
    
    a1=Label(t,text='Employee ID',bg='#FFEDD1')
    a1.place(x=100,y=110)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=400,y=110)
    
    a2=Label(t,text='Holiday Name',bg='#FFEDD1')
    a2.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=400,y=150)
    
    a3=Label(t,text='Number of Leaves',bg='#FFEDD1')
    a3.place(x=100,y=190)
    e3=Entry(t,width=30)
    e3.place(x=400,y=190)
    
    bt=Button(t,text='UPDATE',command=updatedata,bg='#C0C0C0')
    bt.place(x=150,y=320)
    
    bt=Button(t,text='FIND',command=finddata,bg='#C0C0C0')
    bt.place(x=250,y=320)
    
    bt=Button(t,text='Close',command=close,bg='#C0C0C0')
    bt.place(x=350,y=320)
    
    t.mainloop()