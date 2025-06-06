import tkinter 
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox
from maindashboard import *
import pymysql
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

t=tkinter.Tk()
t.geometry('600x600')

d=Canvas(t,width=600,height=600)
d.place(x=0,y=0)

d.create_rectangle(20,20,580,580,fill='black')
d.create_rectangle(25,25,575,575,fill='#90EE90')

# OTP global variable
otp_generated = ""

def forget():
    global otp_generated
    fwin = Toplevel(t)
    fwin.geometry('400x400')
    fwin.title('Forget Password')

    Canvas(fwin, width=400, height=400, bg='#FFD580').place(x=0, y=0)

    Label(fwin, text='Forget Password', font=('Arial', 20), bg='#FFD580').place(x=80, y=30)
    Label(fwin, text='Enter your Email:', bg='#FFD580').place(x=50, y=100)

    e3 = Entry(fwin, width=40)
    e3.place(x=50, y=130)

    def send_otp():
        nonlocal e3, fwin
        email_id = e3.get()
        if email_id == '':
            messagebox.showinfo('Message', 'Please enter your Email ID.')
            return

        # Generate a 6-digit OTP
        otp_generated = str(random.randint(100000, 999999))

        # Compose the email
        from_address = "gautkana432@gmail.com"
        to_address = email_id
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Your OTP for Password Reset'
        msg['From'] = from_address
        msg['To'] = to_address

        html = f"<html><body><h3>Your OTP is: {otp_generated}</h3></body></html>"
        part1 = MIMEText(html, 'html')
        msg.attach(part1)

        # Credentials
        username = 'gautkana432@gmail.com'
        password = 'fqukfesbedilflss'  # App password recommended

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()

            with open('otpsend.txt', 'w') as f:
                f.write(email_id + " " + otp_generated)
            
            messagebox.showinfo('Message', 'OTP has been sent to your email.')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to send email: {str(e)}')

    bt1 = Button(fwin, text='Send OTP', command=send_otp, bg='white')
    bt1.place(x=150, y=180)


def check():
    db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
    cur=db.cursor()
    xa=e1.get()
    xb=e2.get()
    sql="select count(*) from login where loginid='%s' and  password='%s' "%(xa,xb)
    cur.execute(sql)
    data=cur.fetchone()
    if data [0]==0:
        messagebox.showinfo('Message','Account is not found.')
    else:
        showmaindashboard()
    db.close()
            
def signup():
    d=Canvas(t,width=600,height=600)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,580,580,fill='black')
    d.create_rectangle(25,25,575,575,fill='#FFD580')
    
    def cts():
        d.destroy()
        
    def lts():
        d.destroy()
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        sql="select count(*) from login where loginid='%s' and  password='%s' "%(xa,xb)
        cur.execute(sql)
        data=cur.fetchone()
        if data [0]==0:
            if e1.get()=='' and e2.get()=='':
                messagebox.showinfo('Message','Pls fill all columns.')
            else:
                dc=pymysql.connect(host='localhost',user='root',password='root',database='esm')
                cur=dc.cursor()
                xa=e1.get()
                xb=e2.get()
                sql="insert into login values('%s','%s')"%(xa,xb)
                cur.execute(sql)
                dc.commit()
                messagebox.showinfo('Message','Your account is created successfully.')
                cts()
                dc.close()
        else:
            messagebox.showinfo('Message for You','Your account is already exist.')
            cts()
        db.close()

    h1=Label(d,text='Sign Up',font=('arial',20),bg='#FFD580')
    h1.place(x=150,y=60)

    a1=Label(d,text='Email',font=(4),bg='#FFD580')
    a1.place(x=80,y=150)
    e1=Entry(d,width=40)
    e1.place(x=80,y=180)

    a2=Label(d,text='Password',font=(4),bg='#FFD580')
    a2.place(x=80,y=230)
    e2=Entry(d,width=40,show='*')
    e2.place(x=80,y=260)

    bt=Button(d,text='Sign up',command=savedata,bg='white')
    bt.place(x=160,y=310)
    
    a3=Label(d,text="Back to Login.",font=(4),bg='#FFD580')
    a3.place(x=120,y=350)
    
    bt=Button(d,text='Login',command=lts,bg='white')
    bt.place(x=280,y=350)


h1=Label(t,text='Login',font=('arial',20),bg='#90EE90')
h1.place(x=170,y=60)

a1=Label(t,text='UserID',font=(4),bg='#90EE90')
a1.place(x=80,y=150)
e1=Entry(t,width=40)
e1.place(x=80,y=180)

a2=Label(t,text='Password',font=(4),bg='#90EE90')
a2.place(x=80,y=230)
e2=Entry(t,width=40,show='*')
e2.place(x=80,y=260)

bt=Button(t,text='Forget Password',command=forget,bg='white')
bt.place(x=225,y=280)

bt=Button(t,text='Login',command=check,bg='white')
bt.place(x=160,y=350)

a3=Label(t,text="Need an Account?",font=(4),bg='#90EE90')
a3.place(x=90,y=390)

bt=Button(t,text='Sign Up',command=signup,bg='white')
bt.place(x=290,y=390)

t.mainloop()