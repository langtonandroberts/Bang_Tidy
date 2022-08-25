from faulthandler import disable
from tkinter import*
from tkinter import messagebox
from turtle import left, window_width
import backend


#,,,this is the frontend that gives input to the listbox and database (backend)
def get_selected_row(event):
    global selected_tuple
    b3["state"]="disabled"
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
        
def view_command():
    list1.delete(0,END)
    b3["state"]="active"

    for row in backend.view():
        list1.insert(END,row)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
          
def add_command():
    e1=title_text.get()
    e2=author_text.get()
    e3=year_text.get()
    e4=isbn_text.get()
    if e1=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter Title")
    elif e2=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter Autor")
    elif e3=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter Year")
    elif e4=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter ISBN")
    
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def delete_command():
    backend.delete(selected_tuple[0])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
window=Tk()
window.wm_title("Book Store")

# ,,, make start up screen fit any monitor ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
width_value=window.winfo_screenwidth()
height_value=window.winfo_screenheight()
window.geometry(f"{width_value}x{height_value}+0+0")

frame=Frame(window)  
frame.grid(row=0,column=0,pady=10,padx=10)

l1 = Label(frame,text="Title",padx=0,pady=0)
l1.grid(row=0,column=0)

l2 = Label(frame,text="Author")
l2.grid(row=0,column=2)

l3 = Label(frame,text="Year")
l3.grid(row=1,column=0)

l4 = Label(frame,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(frame,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(frame,textvariable=author_text)
e2.grid(row=0,column=3,pady=5)

year_text=StringVar()
e3=Entry(frame,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(frame,textvariable=isbn_text)
e4.grid(row=1,column=3,pady=5)

list1=Listbox(frame,height=6,width=35)
list1.grid(row=1,column=0,rowspan=6,columnspan=2)


sb1=Scrollbar(frame)
sb1.grid(row=2,column=2,rowspan=4,sticky=NS)
sb1.configure(command=list1.yview)
list1.configure(yscrollcommand=sb1.set)
list1.bind("<<ListboxSelect>>",get_selected_row,)


b1=Button(frame,text="View all",width=16,command=view_command)
b1.grid(row=2,column=3,pady=1,padx=5)

b2=Button(frame,text="Search entry",width=16,command=search_command)
b2.grid(row=3,column=3,pady=2)

b3=Button(frame,text="Add entry",width=16,command=add_command)
b3.grid(row=4,column=3,pady=2)

b4=Button(frame,text="Update selection",width=16,command=update_command)
b4.grid(row=5,column=3,pady=2)

b5=Button(frame,text="Delete selection",width=16,command=delete_command)
b5.grid(row=6,column=3,pady=2)

b6=Button(frame,text="Close",width=16,command=window.destroy)
b6.grid(row=7,column=3,pady=2)

e1.focus()


window.mainloop()

