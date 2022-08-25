from tkinter import *

#how to set up 
# ,,,,,,,, window config ,,,,,,,,,,,,,,,,
window=Tk()
window.title("start of programming FIRST WINDOW")
window.geometry()
window.config(background="black")

# ,,,,,,, label property ,,,,,,,,,,,,,,,,,
# photo=PhotoImage(file="location of file\name of file.png")
#Label=Label(window,
            #text="HELLO WORLD",
            #font=("Arial",25,"bold"),
            #fg="#9bb7c2",#HEX Color
            #bg="#cbf2f0",
            #relief=RAISED,# SUNKEN
            #bd=5,
            #padx=10,
            #pady=10)
            #image=photo,
            # compound="bottom")

#Label.place(x=80,y=100)#pack()


# ,,,,,,,,, frame ,,,,,,,,,,,,,,,,
frame0=Frame(window,bg="green",highlightbackground="#f2faf9",highlightthickness=2)#frame and every thing placed in it.
frame0.grid(row=0,column=0,padx=1,pady=1,ipadx=20,ipady=20)#place(x=50,y=100)


frame1=Frame(frame0,width=100,bg="red",highlightbackground="blue",highlightthickness=2)#frame and every thing placed in it.
frame1.grid(row=1,column=0,padx=10,pady=10,ipadx=60,ipady=80)

frame2=Frame(frame0,width=100,bg="yellow",highlightbackground="blue",highlightthickness=2)#frame and every thing placed in it.
frame2.grid(row=1,column=1,padx=10,pady=10,ipadx=60,ipady=80)

frame3=Frame(frame0,width=100,bg="pink",highlightbackground="#f2faf9",highlightthickness=2)#frame and every thing placed in it.
frame3.grid(row=1,column=2,padx=10,pady=10,ipadx=60,ipady=80)#place(x=50,y=100)

frame4=Frame(frame0,width=100,bg="blue",highlightbackground="blue",highlightthickness=2)#frame and every thing placed in it.
frame4.grid(row=1,column=3,padx=10,pady=10,ipadx=60,ipady=80)

lbl=Label(frame1,text="ONE")#,fg="#265e78",background="#6aadcc",font=10)
lbl.place(x=5,y=100)#grid(row=0,column=0)#,sticky=EW,padx=0,pady=0)#place(x=5,y=155)
lb2=Label(frame2,text="TWO")#,fg="#265e78",background="#6aadcc",font=10)
lb2.place(x=5,y=100)#grid(row=0,column=0)#,sticky=EW,padx=0,pady=0)#place(x=5,y=155)
lb3=Label(frame3,text="THREE")#,fg="#265e78",background="#6aadcc",font=10)
lb3.place(x=5,y=100)#grid(row=0,column=0)#,sticky=EW,padx=0,pady=0)#place(x=5,y=155)
lb4=Label(frame4,text="FOUR")#,fg="#265e78",background="#6aadcc",font=10)
lb4.place(x=5,y=100)#grid(row=0,column=0)#,sticky=EW,padx=0,pady=0)#place(x=5,y=155)

#textbox=Entry(frame1,fg="#fc9fe2",font=10)
#textbox.grid(row=0,column=1,sticky=EW,padx=0,pady=0)#place(x=5,y=5)
#button1=Button(frame1,text="Save",fg="#4487a6",font=10,relief=RAISED,bd=1)
#button1.grid(row=0,column=0,sticky=EW,padx=10,pady=60)#place(x=5,y=82)



window.mainloop() # ,,, this puts window on screen ,,,,,,