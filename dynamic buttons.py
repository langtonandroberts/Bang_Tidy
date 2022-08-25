

# Dynamic Buttons
#https://youtu.be/QF68u45tQB4

import tkinter as tk 
from tkinter import *

my_w = tk.Tk()
my_w.geometry('300x200')# window size

font1=('Times',16,'normal')
n=4 #number of buttons


def my_fun(k):
    my_str.set("Btn No is : " + str(k))#convert value of k into a string.(which is the value of j)
    

for j in range(n):#puts a button on screen for every number in (n)
    e=Button(my_w,text=j,font=font1,command=lambda k=j:my_fun(k))
    e.grid(row=3,column=j,padx=2,pady=2)#column=j puts buttons next to each other

my_str=tk.StringVar()
l1=tk.Label(my_w,textvariable=my_str,width=10,font=font1)
l1.grid(row=1,column=2,columnspan=n)#(n) is number of buttons.

def show_lan(my_language,var):
    my_str.set(my_language)
    for i in range(len(buttons)):
        if i ==var:
            buttons[i].config(state='disabled')#disables button after it has been clicked.
        else:
            buttons[i].config(state='normal')

var=0
buttons=[]
list_languages=('PHP','Python','HTML','JS')

for language in list_languages:#puts a button on screen for every iteam in buttons list.
    btn=Button(my_w,text=language,font=font1,command=lambda var=var,lan=language:show_lan(lan,var))
    btn.grid(row=2,column=var,padx=2)
    var += 1
    buttons.append(btn)




my_w.mainloop()#keep the window open
