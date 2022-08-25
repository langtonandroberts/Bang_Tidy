

#,,,, this code links Combo boxes together.
#,,,, also this code links list boxes together.

from logging import root
from tkinter import*
from tkinter import ttk

root=Tk()
root.title("Dependent List Box")
root.geometry("500x400")

#,,,,,Combo box values,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# ,,, creating a value (list) of sizes [],,,,,,,,,,,,,,
department=[
    "Boarding",
    "Daycare",
    "Grooming"]

# ,,, creat a list of colours ,,,,
boarding_service=[
    "Extra feed",
    "Mixed exercise pen",
    "Play Time",
    "Remote Viewing"]

daycare_service=[
    "Swim",
    "Walk"]

grooming_service=[
    "Shampoo",
    "Nails"]

discrption=["Extra feed portion."]

#,, function when colour in combo box picked,,,,,,,,,,,,,,
def pick_colour(e):
    if my_combo.get()== "Boarding":
        colour_combo.config(value=boarding_service)
        colour_combo.current(0)
    if my_combo.get()== "Daycare":
        colour_combo.config(value=daycare_service)
        colour_combo.current(0)
    if my_combo.get()== "Grooming":
        colour_combo.config(value=grooming_service)
        colour_combo.current(0)
    
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# ,,, create (combo box 1),,,,,,,,,,,,,,,,,,,,,,,,
my_combo=ttk.Combobox(root,value=department)#,,value is the list alicated to sizes[].
my_combo.current(0)
my_combo.pack(pady=20)
# ,,, bind combo box (link to function),,,,,,,,,,,,,,,,,,,
my_combo.bind("<<ComboboxSelected>>",pick_colour)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# ,,, create (combo box 2),,,,,,,,,,,,,,,,,,,,,,,,
colour_combo=ttk.Combobox(root,value=[" "])
colour_combo.current(0)
colour_combo.pack(pady=20)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# ,,,List box Frame and list box,,,,,,,,,,,,,,,,,,,,,,,,,,,
my_frame=Frame(root)
my_frame.pack(pady=50)
my_list1=Listbox(my_frame)
my_list1.grid(row=0,column=0)
my_list2=Listbox(my_frame)
my_list2.grid(row=0,column=1,padx=20)
my_list3=Listbox(my_frame)
my_list3.grid(row=0,column=2,padx=20)


#,,,Function when item in my_list1 box clicked,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
def list_colour(e):
    my_list2.delete(0,END)#,,this clears last entered items in the listbox.
    if my_list1.get(ANCHOR)=="Boarding":
        for item in boarding_service:
            my_list2.insert(END,item)
    if my_list1.get(ANCHOR)=="Daycare":
        for item in daycare_service:
            my_list2.insert(END,item)
    if my_list1.get(ANCHOR)=="Grooming":
        for item in grooming_service:
            my_list2.insert(END,item)#,,inserts values to another list box.

            
#,,,Function when item in my_list1 box clicked,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
def info(e):
    my_list3.delete(0,END)#,,this clears last entered items in the listbox.
    if my_list2.get(ANCHOR)=="Extra feed":
        for item in discrption:
            my_list3.insert(END,item)
    if my_list1.get(ANCHOR)=="Daycare":
        for item in daycare_service:
            my_list3.insert(END,item)
    if my_list1.get(ANCHOR)=="Grooming":
        for item in grooming_service:
            my_list3.insert(END,item)#,,inserts values to another list box.           
        
# ,,, Add's item values to list box,,,,,,,,,,,,,,,,,,,,,,
for item in department:
    my_list1.insert(END,item)

# ,,, bind listbox to function,,,,,,,,,,,,,,,,
my_list1.bind("<<ListboxSelect>>",list_colour)
my_list2.bind("<<ListboxSelect>>",info)


root.mainloop()


