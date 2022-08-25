from tkinter import*
my_window=Tk()



#var_1=StringVar()
var_2=StringVar()

#e=Button(my_window,text="Click me")
#e.pack()

label_1=Label(my_window,
              relief="solid",
              font="Times 22 bold",
              #textvariable=var_1
              )


label_2=Label(my_window,
              relief="solid",
              font="Times 22 bold",
              textvariable=var_2
              )

label_1.pack()
label_2.pack()

#var_1.set('Enclosure')
label_1 ['text']='New text'
var_2.set('New')


my_window.mainloop()