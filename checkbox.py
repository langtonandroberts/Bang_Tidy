from tkinter import *


def display():
    if (x.get()==1):#(x.get())returns true or faulse/#could use == Yes or No.
        print('You agree!')
    else:
        print('You dont agree.')

window=Tk()

x = IntVar()#could be booleanVar/StringVar

#photo=PhotoImage(file='use file path or file name')

check_button = Checkbutton(window,
                           text='I agree to somthing',
                           variable=x,
                           onvalue=1,#could use Yes or No.
                           offvalue=0,#could use Yes or No.
                           font=('Arial',15),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           #image=photo,
                           #commpound='left',
                           command=display)

check_button.pack()
window.mainloop()