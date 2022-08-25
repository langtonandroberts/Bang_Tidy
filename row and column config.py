

#https://youtu.be/Wf0JT9dieGw

import tkinter as tk 
from tkinter import * 
my_window=tk.Tk()
my_window.geometry("1000x700")#size of window
my_window.columnconfigure(0,weight=1)#colum 0 is the only column in the window.
my_window.columnconfigure(1,weight=3)#colum 0 is the only column in the window.
my_window.columnconfigure(2,weight=1)#colum 0 is the only column in the window.

my_window.rowconfigure(0,weight=1)
my_window.rowconfigure(1,weight=8)
my_window.rowconfigure(2,weight=2)

#frames will not show intill you put something in them.
frame_top=tk.Frame(my_window,bg="red")
frame_middle=tk.Frame(my_window,bg="yellow")
frame_bottom=tk.Frame(my_window,bg="blue")
frame_left=tk.Frame(my_window,bg="light green")
frame_right=tk.Frame(my_window,bg="green")
frame_top.grid(row=0,column=1,sticky="WENS")
frame_middle.grid(row=1,column=1,sticky="WENS")
frame_bottom.grid(row=2,column=1,sticky="WENS")
frame_left.grid(row=0,column=0,rowspan=3,sticky="WENS")
frame_right.grid(row=0,column=2,rowspan=3,sticky="WENS")

#l1=tk.Label(frame_top,text="frame top")
#l1.grid(row=0,column=0,padx=10,pady=2)
l1=tk.Label(frame_middle,text="frame middle")
l1.grid(row=0,column=0,padx=10,pady=2)
l1=tk.Label(frame_bottom,text="frame bottom")
l1.grid(row=0,column=0,padx=10,pady=2)

frame_top.columnconfigure(0,weight=1)
frame_middle.columnconfigure(1,weight=1)
frame_bottom.columnconfigure(2,weight=1)

#Top frame given 3 columns
frame_top.columnconfigure(0,weight=1)
frame_top.columnconfigure(1,weight=1)
frame_top.columnconfigure(2,weight=1)

#Tree labels placed in Top frame.
l1=tk.Label(frame_top,text="Left")
l1.grid(row=0,column=0,padx=10,pady=2)
l1=tk.Label(frame_top,text="Middle")
l1.grid(row=0,column=1,padx=10,pady=2)
l1=tk.Label(frame_top,text="Right")
l1.grid(row=0,column=2,padx=10,pady=2)


my_window.mainloop()
