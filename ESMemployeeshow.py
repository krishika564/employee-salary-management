import pymysql
from tkinter import messagebox
import tkinter
from tkinter import *
from tkinter import ttk

def showESMemployeeshow():
    
    t=tkinter.Tk()
    t.geometry('700x700')
    
    d=Canvas(t,width=700,height=700)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,680,680,fill='black')
    d.create_rectangle(25,25,675,675,fill='#FFEDD1')
    
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='ESM')
        cur=db.cursor()
        sql="select * from Employee"
        cur.execute(sql)
        data=cur.fetchall()
        msg=""
        for res in data:
            msg=msg+str(res[0])+"\t"
            msg=msg+str(res[1])+"\t"
            msg=msg+str(res[2])+"\t"
            msg=msg+str(res[3])+"\t"
            msg=msg+str(res[4])+"\t"
            msg=msg+str(res[5])+"\t"
            msg=msg+str(res[6])+"\t"
            msg=msg+"\n"
        db.close()
        w.insert(END,msg)
        
    w=Text(t,width=78,height=30)
    w.place(x=30,y=30)
    filldata()
    t.mainloop()