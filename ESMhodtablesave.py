import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMhodtablesave():
    
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
        sql="select deptid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e3['values']=lt
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showerror('Hi','Pls fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=int(e3.get())
            xd=e4.get()
            sql="insert into HODTable values (%d,'%s',%d,'%s')" %(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('hi','Save')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            db.close()
            
    def close():
        t.destroy()
    
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
    e3=ttk.Combobox(d)
    filldata()
    e3.place(x=400,y=190)
    
    a4=Label(t,text='Remarks',bg='#FFEDD1')
    a4.place(x=100,y=230)
    e4=Entry(t,width=30)
    e4.place(x=400,y=230)
    
    bt=Button(t,text='SAVE',command=savedata,bg='#C0C0C0')
    bt.place(x=250,y=320)
    
    bt=Button(t,text='Close',command=close,bg='#C0C0C0')
    bt.place(x=350,y=320)
    
    t.mainloop()