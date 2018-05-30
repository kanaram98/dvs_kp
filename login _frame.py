from tkinter import *
win =Tk()
def fun(event):
    print("welcome to eevnet")
win.geometry("1920x900")
#frame=Frame(win,height=200,width=400)
#frame.pack()
name=Label(win,text="User Name ",bg="yellow",font=11)
password=Label(win,text="Password ",bg="yellow",font=11)
email=Label(win,text="Email ID ",bg="yellow",font=11)
name.grid(row=3,column=2,sticky=E)
password.grid(row=4,column=2,sticky=E)
email.grid(row=5,column=2,sticky=E)
entery1=Entry(win,justify=LEFT,width=30,bd=5,font=11,highlightcolor='blue')
entery2=Entry(win,width=30,bd=5,font=11,exportselection=1,show="*")
entery3=Entry(win,width=30,bd=5,font=11,cursor="arrow",selectborderwidth=1,selectbackground="red",selectforeground="pink")
entery1.grid(row=3,column=4)
entery2.grid(row=4,column=4)
entery3.grid(row=5,column=4)
check =Checkbutton(win,highlightcolor='blue',font=11,text="keep me login")#state=DISABLED
check.grid(columnspan=5)

button=Button(win,text="login")
button.bind("<Button-1>",fun)
button.grid(columnspan=5)
##frame=Frame(win,height=200,width=400)
#frame.pack()

win.mainloop()
