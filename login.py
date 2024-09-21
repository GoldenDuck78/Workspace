import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


app = tk.Tk()
app.geometry('600x400')
def lay2():
    sinhvien = mysql.connector.connect(
        host = "localhost",
        user= "root",
        password = "root",
        database = "test"
    )
    mycursor = sinhvien.cursor()
    lay2 = tk.Tk()
    lay2.columnconfigure(0, weight = 1)
    lay2.columnconfigure(0, weight = 2)
    msv = tk.StringVar()
    main_frame = tk.Frame(lay2,bg = 'wheat', width = 200, height = 200, relief='raised', bd = 5)
    
    
    msv_label = tk.Label(main_frame,text="MA SINH VIEN: ", font = ("Arial",13,'bold')). grid(row = 0, column=0)
    msv_entry = tk.Entry(main_frame,textvariable=msv). grid(row = 0, column=1)
    
    
def lay3():
    lay3 = tk.Toplevel()
    tab_control = ttk.Notebook(lay3)
    
    tab1 = tk.Frame(tab_control)
    tab2 = tk.Frame(tab_control)
    tab_control.add(tab1,text= "Nhap diem")
    tab_control.add(tab2,text="Thong ke")
    tab_control.pack(expand=1, fill='both')
    
    tab1_frame = tk.Frame(tab1,height=500, width = 550, bg='wheat',relief='raised', borderwidth=10)
    tab1_frame.pack()
    tab1_frame.grid_propagate(False)

    msv = tk.StringVar()
    mgv = tk.StringVar()
    mhp = tk.StringVar()
    dgk = tk.DoubleVar()
    dck = tk.DoubleVar()

    def reset() :
        msv.set("")
        mgv.set("")
        mhp.set("")
        dgk.set(0.0)
        dck.set(0.0)
        

    msv_lable = tk.Label(tab1_frame,text= "MA SINH VIEN: ", font=('Arial',13)).grid(row=0, column=0, padx=5, pady=5,sticky=tk.E)
    msv_entry = tk.Entry(tab1_frame,width=40,textvariable=msv, bd= 2).grid(row= 0, column=1, sticky=tk.W)

    mgv_label = tk.Label(tab1_frame, text='MA GIANG VIEN: ', font=("Arial",13)).grid(row=1,column=0,padx= 5,pady=5,sticky=tk.E)
    mgv_entry = tk.Entry(tab1_frame, width=40, textvariable=mgv,bd =2).grid(row=1, column=1, sticky=tk.W)

    mhp_lable = tk.Label(tab1_frame, text='MA HOC PHAN: ', font=("Arial",13)).grid(row=2,column=0,padx= 5,pady=5,sticky=tk.E)
    mhp_entry = tk.Entry(tab1_frame, width=40,textvariable=mhp, bd =2).grid(row=2, column=1, sticky=tk.W)

    dgk_label = tk.Label(tab1_frame, text='DIEM GIUA KI: ', font=("Arial",13)).grid(row=3,column=0,padx= 5,pady=5,sticky=tk.E)
    dgk_entry = tk.Entry(tab1_frame, width=20, textvariable=dgk,bd =2).grid(row=3, column=1, sticky=tk.W)

    dck_label = tk.Label(tab1_frame, text='DIEM CUOI KI: ', font=("Arial",13)).grid(row=4,column=0,padx= 5,pady=5,sticky=tk.E)
    dck_entry = tk.Entry(tab1_frame, width=20,textvariable=dck, bd =2).grid(row=4, column=1, sticky=tk.W)
    def haveSubmit():
        bangdiem = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="root",
            database = "test"
        )
        mycursor = bangdiem.cursor()
        
        sql = "INSERT INTO bangdiem(msv,mgv,mhp,dgk,dck) VALUES (%s,%s,%s,%s,%s)"
        mycursor.execute(sql,(msv.get(),mgv.get(),mhp.get(),dgk.get(),dck.get()))
        bangdiem.commit()
        bangdiem.close()
        messagebox.showinfo("Da them 1 record","MSV: " + str(msv), "\nMGV: " + str(mgv) +"\nMHP: " +str(mhp) + "\nDGK: " + str(dgk) + "\nDCK: " + str(dck))
        
        
    submit_btn = tk.Button(tab1_frame,text="Xac nhan",bd = 5,width=15,relief='raised', command=haveSubmit).grid(row=5,column=1, columnspan=2,sticky=tk.W)
    reset_btn = tk.Button(tab1_frame,text="Nhap lai",bd = 5,width=15, relief='raised', command=reset).grid(row=5,column=1,columnspan=2,sticky=tk.E, padx= 5)
    
    
        
    # tab bang diem
    bangDiem = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = 'test'
    )

    mycursor = bangDiem.cursor()
    mycursor.execute("SELECT * FROM bangDiem")
    label_frame = tk.LabelFrame(tab2,text="BANG THONG KE",bg="wheat", font=("Arial",20,"bold"), borderwidth = 5)

    title1= tk.Label(label_frame,text="Ma sinh vien", width = 20,borderwidth=1, relief='solid')
    title2= tk.Label(label_frame,text="Ma giang vien", width = 20,borderwidth=1, relief='solid')
    title3 = tk.Label(label_frame,text="Ma hoc phan", width = 20,borderwidth=1, relief='solid')
    title4 = tk.Label(label_frame,text="Diem giua ki", width = 20,borderwidth=1, relief='solid')
    title5 = tk.Label(label_frame,text="Diem cuoi ki", width = 20,borderwidth=1, relief='solid')
    row = 1
    for i in mycursor.fetchall():
        for j in range(5):
            index = tk.Label(label_frame,text=i[j],width = 20, borderwidth=1, relief='solid').grid(row = row,column=j)
        row+=1

    title1.grid(row=0,column=0)
    title2.grid(row=0,column=1)
    title3.grid(row=0,column=2)
    title4.grid(row=0,column=3)
    title5.grid(row=0,column=4)
    label_frame.pack(fill='y',expand="yes")

    lay3.mainloop()

main_frame = tk.Frame(app,bg = 'wheat', width = 400, height = 200, relief ='raised', borderwidth=5)
main_frame.grid_propagate(0)
user_var = tk.StringVar()
password_var = tk.StringVar()
user_label = tk.Label(main_frame,bg="wheat", text="MSV: ", font=("Arial",13,"bold")).grid(row=0,column=0,sticky=tk.E)
password_label = tk.Label(main_frame,bg="wheat",text="MAT KHAU: ", font=("Arial",13,"bold")).grid(row=1,column=0, sticky=tk.E)
user_entry = tk.Entry(main_frame, textvariable=user_var,width=30)
password_entry = tk.Entry(main_frame,textvariable=password_var,width = 30,show = '*')

def validate():
    taikhoan = mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "root",
        database = "account"
    )
    if user_var.get() == "":    
        messagebox.showinfo("Lỗi","Hãy nhập mã sinh viên!")
        user_entry.focus()
    elif password_var.get() == "":
        messagebox.showinfo("Lỗi","Hãy nhập mật khẩu!")
        password_entry.focus()
        
    mycursor = taikhoan.cursor()
    sql = "SELECT * FROM account.account WHERE user = %s"
    mycursor.execute(sql,(user_var.get(),))
    if not mycursor.fetchone():
        messagebox.showinfo("Loi","Khong thay ma sinh vien")
    
    mycursor.execute(sql,(user_var.get(),))
    if mycursor.fetchone()[1] == password_var.get():
        lay2()
    else:
        messagebox.showinfo("Loi","Sai mat khau")
    
    
    


logIn = tk.Button(main_frame,text="Log in",width =  15,command=validate)
user_entry.grid(row = 0, column = 1, padx=5,sticky=tk.W ,pady= 5)
password_entry.grid(row = 1, column = 1, padx= 5,sticky=tk.W ,pady=5)
logIn.grid(row=2,column=1, columnspan=2,sticky=tk.W,padx = 5,pady=5)
main_frame.pack()

app.mainloop() 