import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

def showESMempsalarydelete():
    
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
    
    def delete(): 
        db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from Empsalary where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','Deleted')
        e1.delete(0,100)
        db.close()
    
    b1=Label(t,text="Employee Salary Management",fg='darkblue',font=('arial',10),bg='#FFEDD1')
    b1.place(x=300,y=40)
    b2=Label(t,text='Employee Salary',bg='#FFEDD1')
    b2.place(x=350,y=70)
    
    a1=Label(t,text='Employee ID',bg='#FFEDD1')
    a1.place(x=100,y=110)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=400,y=110)
    
    bt=Button(t,text='DELETE',command=delete,bg='#C0C0C0')
    bt.place(x=350,y=320)
    
    t.mainloop()