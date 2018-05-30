import tkinter as tk


def clicked():
	print("button was clicked")


	
w=tk.Tk()
##screen_width = w.winfo_screenwidth()
##screen_height = w.winfo_screenheight()
w.title("clinic managment")
w.geometry('1530x780')
w.resizable(0, 0)
m=tk.Menu(w)
w.config(menu=m)
submenu_file=tk.Menu(m)
submenu_edit=tk.Menu(m)
m.add_cascade(label="ADD Doctor",menu=submenu_file,command=clicked)
#m.add_cascade.pack()
m.add_cascade(label="Add Receptionist",menu=submenu_edit)
m.add_cascade(label="View Patient",menu=submenu_edit)
m.add_cascade(label="View doctor",menu=submenu_edit)
m.add_cascade(label="View Reception",menu=submenu_edit)
m.add_cascade(label="Change password",menu=submenu_edit)
m.add_cascade(label="logout",menu=submenu_edit)
submenu_file.add_command(label="new entry",command=clicked)
submenu_file.add_separator()
submenu_file.add_command(label="open",command=clicked)
submenu_file.add_separator()
submenu_file.add_command(label="setting",command=clicked)
submenu_edit.add_command(label="copy",command=clicked)


w.mainloop()
