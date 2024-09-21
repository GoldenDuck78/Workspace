import tkinter as tk

gd = tk.Tk()
gd.geometry('1000x600')
main_frame = tk.Frame(gd,height=500, width=700, bg='wheat',relief='raised', borderwidth=10)
main_frame.pack()
main_frame.grid_propagate(False)
main_frame.columnconfigure(0,weight=1)
main_frame.columnconfigure(1,weight=1)

mph = tk.StringVar()
gv = tk.StringVar()
thp = tk.StringVar()
dgk = tk.DoubleVar()
dck = tk.DoubleVar()

def reset() :
    mph.set("")
    gv.set("")
    thp.set("")
    dgk.set(0.0)
    dck.set(0.0)
    

mhp_label = tk.Label(main_frame,text= "MA HOC PHAN: ", font=('Arial',13)).grid(row=0, column=0, padx=5, pady=5,sticky=tk.E)
mhp_entry = tk.Entry(main_frame,width = 40,textvariable=mph, bd= 2).grid(row= 0, column=1, sticky=tk.W)

gv_label = tk.Label(main_frame, text='GIAO VIEN CO VAN: ', font=("Arial",13)).grid(row=1,column=0,padx= 5,pady=5,sticky=tk.E)
gv_entry = tk.Entry(main_frame, width=40, textvariable=gv,bd =2).grid(row=1, column=1, sticky=tk.W)

thp_label = tk.Label(main_frame, text='TEN HOC PHAN: ', font=("Arial",13)).grid(row=2,column=0,padx= 5,pady=5,sticky=tk.E)
thp_entry = tk.Entry(main_frame, width=40,textvariable=thp, bd =2).grid(row=2, column=1, sticky=tk.W)

dgk_label = tk.Label(main_frame, text='DIEM GIUA KI: ', font=("Arial",13)).grid(row=3,column=0,padx= 5,pady=5,sticky=tk.E)
dgk_entry = tk.Entry(main_frame, width=20, textvariable=dgk,bd =2).grid(row=3, column=1, sticky=tk.W)

dck_label = tk.Label(main_frame, text='DIEM CUOI KI: ', font=("Arial",13)).grid(row=4,column=0,padx= 5,pady=5,sticky=tk.E)
dck_entry = tk.Entry(main_frame, width=20,textvariable=dck, bd =2).grid(row=4, column=1, sticky=tk.W)

dgk_label = tk.Label(main_frame, text='DIEM GIUA KI: ', font=("Arial",13)).grid(row=5,column=0,padx= 5,pady=5,sticky=tk.E)
dgk_entry = tk.Entry(main_frame, width=20, bd =2).grid(row=5, column=1, sticky=tk.W)

submit_frame = tk.Frame(main_frame).grid(rowspan = 2,columnspan=2)
submit_btn = tk.Button(main_frame,text="Xac nhan",bd = 5,relief='raised').grid(row=6,column=0,sticky=tk.E)
reset_btn = tk.Button(main_frame,text="Nhap lai",bd = 5, relief='raised', command=reset).grid(row=6,column=1,sticky=tk.W, padx= 5)

gd.mainloop()