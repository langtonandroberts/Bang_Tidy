from cgitb import text
#from curses import Textpad
from distutils import text_file
from tkinter import*
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os,sys
from tkinter import messagebox
from folium import Popup
import win32print
import win32api



root=Tk()
root.title('Text Box Sample')
root.geometry('650x450')

# Read only r
# Read and write r+ (beginning of file)
# Write Only w (over-written)
# Write and Read w+ (over-written)
# Append Only a (end of file)
# Append and Read a+ (end of file)
global open_status_name
open_status_name=False
global selected
selected=False


def save_text():
    text_file=filedialog.askopenfilename(initialdir="C:/gui/",title="Open Text File",filetypes=(("Text Files", "*.txt"),))
    text_file=open(text_file,'w')
    text_file.write(my_text.get(1.0,END))

def clear():
    my_text.delete(1.0,END)#,,,textbox starts at 1.0.

def get_text():
    my_label.config(text=my_text.get(1.0,END))#,,you can get 1 line(1.0,2.0)stops 1 line before.

def open_text():
    my_text.delete(1.0,END)#,,,textbox starts at 1.0.
    text_file=filedialog.askopenfilename(initialdir="C:/gui/",title="Open Text File",filetypes=(("Text Files", "*.txt"),))
    name=text_file
    name=name.replace(".txt","")#,,remove any text in opened window,
    text_file=open(text_file,'r')
    stuff=text_file.read()
    
    my_text.insert(END,stuff)
    text_file.close()
    root.title(f'{name} - Textpad')

def add_image():    
    #,,,add image
    global my_image
    my_image=PhotoImage(file="2e831102.png")
    position=my_text.index(INSERT)
    my_text.image_create(position,image=my_image)

def select():
    selected=my_text.selection_get()
    my_label.config(text=selected)

def bolder():#,,make font bold.
    bold_font=font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")
    my_text.tag_configure("bold",font=bold_font)
    current_tags=my_text.tag_names("sel.first")
    
    if "bold" in current_tags:
        my_text.tag_remove('bold','sel.first','sel.last')
    else:
        my_text.tag_add('bold','sel.first','sel.last')
        
def italics_it():#,,Make text italic.
    italics_font=font.Font(my_text,my_text.cget("font"))
    italics_font.configure(slant="italic")
    my_text.tag_configure("italic",font=italics_font)
    current_tags=my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove('italic','sel.first','sel.last')
    else:
        my_text.tag_add('italic','sel.first','sel.last')

#,,create new file function. in dropdown menu
def new_file():
    #,,delete previus text
    my_text.delete("1.0",END)
    #,,update status bar
    root.title("New File! - Langton & Roberts TextPad!")#change name in title.
    status_bar.config(text="This is a (fresh) New File!.   ")#change name in bottom.
    global open_status_name
    open_status_name=False

company_name="Langton & Roberts"

#,,open file function
def open_file():
    #,,delete previus text
    my_text.delete("1.0",END)
    #,,Grab file name
    text_file=filedialog.askopenfilename(initialdir="C:/gui/",
                                         title=company_name,
                                         filetypes=(("Text Files","*.txt"),
                                                    ("HTML Files","*.htlm"),
                                                    ("Python Files","*.py"),
                                                    ("All Files","*.*")))
    #,,check to see if there is a file name
    if text_file:
        #,,make filename global so we can access it later.
        global open_status_name
        open_status_name=text_file
    #,,update status bars.
    name=text_file
    status_bar.config(text=f'{name}        ')
    name=name.replace("C:/gui/","")
    root.title(f"{name}-TextPad!")
    #,,open the file
    text_file=open(text_file,'r')#read
    stuff=text_file.read()
    #,,add file to text box.
    my_text.insert(END,stuff)
    #,,close the opened file.
    text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        #,,save the file
        text_file=open(open_status_name,'w')#write
        text_file.write(my_text.get(1.0,END))
        text_file.close()
        status_bar.config(text=f'Saved:{open_status_name}        ')
        messagebox.showinfo("SAVED","Your changes have been saved.")
    else:
        save_as_file() 

def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",
                                           initialdir="C:/gui/",
                                           title="Save File",
                                           filetypes=(("Text Files","*.txt"),
                                                      ("HTML Files","*.html"),
                                                      ("Python Files","*.py"),
                                                      ("All Files","*.*")))
    if text_file:
        #,,update status bars.
        name=text_file
        status_bar.config(text=f'Saved:{name}        ')
        name=name.replace("C:/gui/","")
        root.title(f"{name}-TextPad!")
        #,,save the file
        text_file=open(text_file,'w')#write
        text_file.write(my_text.get(1.0,END))
        text_file.close()
        messagebox.showinfo("SAVED","Your file has been saved.")
                   
                   
#,,cut text,,,,,,,,,
def cut_text(e):
    global selected
    if e:
        selected=root.clipboard_get()
    else:
        if my_text.selection_get():
            #,grab selected text from text box
            selected=my_text.selection_get()
            #,delete selected text from text box
            my_text.delete("sel.first","sel.last")
            #,,clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)

#,,copy text,,,,,,,,
def copy_text(e):
    global selected
    #,,check to see if we used keyboard shortcuts
    if e:
        selected=root.clipboard_get()
        
    if my_text.selection_get():
        #,grab selected text from text box
        selected=my_text.selection_get()
        #,,clear the clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected)
                
#,,paste text,,,,,,,
def paste_text(e):
    global selected
    if e:
        selected=root.clipboard_get()
    else:
        if selected:
            position=my_text.index(INSERT)
            my_text.insert(position,selected)

#,,pick colour.
def text_colour():
    #,,pick colour.
    my_colour=colorchooser.askcolor()[1]
    if my_colour:
        colour_font=font.Font(my_text,my_text.cget("font"))
        my_text.tag_configure("coloured",font=colour_font,foreground=my_colour)
        current_tags=my_text.tag_names("sel.first")
        if "coloured" in current_tags:
            my_text.tag_remove('colored','sel.first','sel.last')
        else:
            my_text.tag_add('coloured','sel.first','sel.last')

#,,change bg colour    
def bg_colour():
    my_colour=colorchooser.askcolor()[1]
    if my_colour:
        my_text.config(bg=my_colour)

#,,change All text colour
def all_text_colour():
    my_colour=colorchooser.askcolor()[1]
    if my_colour:
        my_text.config(fg=my_colour)

#,, print file function,,,Basic file printing.
def print_file():
    printer_name=win32print.GetDefaultPrinter()
    status_bar.config(text=printer_name)
    #,,grab filename any file. not text showing in editor.
    file_to_print=filedialog.askopenfilename(initialdir="C:/gui/",title="Open file to print",filetypes=(("Text Files","*.txt"),("HTML Files","*.htlm"),("Python Files","*.py"),("All Files","*.*")))
    if file_to_print:
        win32api.ShellExecute(0,"print",file_to_print,None,".",0)
        print("Done, File has been printed")

def select_all(e):
    #,,add s.e.l tag to select text
    my_text.tag_add('sel','1.0',"end")#select begining to end.

def clear_all():
    my_text.delete(1.0,END)



#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#,,creates main frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
my_frame=Frame(root)
my_frame.pack(pady=10)

#,,toolbar frame,,,,,,,,,,
toolbar_frame=Frame(my_frame)
toolbar_frame.pack(fill=X)

#,,,create scroll bar.
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)
hor_scroll=Scrollbar(my_frame,orient="horizontal")
hor_scroll.pack(side=BOTTOM,fill=X)

my_text=Text(my_frame,width=50,height=10,font=('helvetica',16),selectbackground='yellow',selectforeground='black',yscrollcommand=text_scroll.set,undo=True,xscrollcommand=hor_scroll.set)
my_text.pack()
#,,,Configure scroll bars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#,,Button frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
button_frame=LabelFrame(root,text='Buttons')
button_frame.pack()

clear_button=Button(button_frame,text='Clear Screen',command=clear)
clear_button.grid(row=0,column=0,padx=3)

get_text_button=Button(button_frame,text='Get Text',command=get_text)
get_text_button.grid(row=0,column=1,padx=3)

open_button=Button(button_frame,text='Open Text File',command=open_text)
open_button.grid(row=0,column=2,padx=3)

save_button=Button(button_frame,text="Save File")#,command=save_text)
save_button.grid(row=0,column=3,padx=3)

image_button=Button(button_frame,text="Add Image",command=add_image)
image_button.grid(row=0,column=4,padx=3)

select_button=Button(button_frame,text="Select Text",command=select)
select_button.grid(row=0,column=5,padx=3)
#,,,,,tool bar buttons,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
bold_button=Button(toolbar_frame,text="Bold",command=bolder)
bold_button.grid(row=0,column=0,sticky=W,padx=1,pady=2)

italics_button=Button(toolbar_frame,text='Italics',command=italics_it)
italics_button.grid(row=0,column=1,padx=1,pady=2)

undo_button=Button(toolbar_frame,text="Undo",command=my_text.edit_undo)
undo_button.grid(row=0,column=2,padx=1,pady=2)

redo_button=Button(toolbar_frame,text="Redo",command=my_text.edit_redo)
redo_button.grid(row=0,column=3,padx=1,pady=2)

#,,text colour
colour_text_button=Button(toolbar_frame,text="Text Colour",command=text_colour)
colour_text_button.grid(row=0,column=4,padx=1,pady=2)


my_label=Label(root,text='')#,,emty.
my_label.pack(pady=20)


#,,create Menu,,,,,,,,,,,,,,,
my_menu=Menu(root)
root.config(menu=my_menu)
#,,add file menu.,,,,,,,,,,,,
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File",command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#,,add edit menu,,,,,,,,,,,,
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda:cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy",command=lambda:copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste",command=lambda:paste_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=lambda:select_all(True),accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear",command=clear_all,accelerator="(Ctrl+y)")

colour_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Colour",menu=colour_menu)
colour_menu.add_command(label="Selected Text",command=text_colour)
colour_menu.add_command(label="All Text",command=all_text_colour)
colour_menu.add_command(label="Background",command=bg_colour)


#,,add status bar to bottom of app,,,,,
status_bar=Label(root,text="Ready, let's get started.            ", anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)

#,,,edit bindings
root.bind("<Control-Key-x>",cut_text)
root.bind("<Control-Key-c>",copy_text)
root.bind("<Control-Key-v>",paste_text)
#,,,select bindings
root.bind('<Control-A>',select_all)
root.bind('<Control-a>',select_all)




root.mainloop()

