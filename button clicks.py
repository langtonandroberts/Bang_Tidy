from cProfile import label
from logging import root
from multiprocessing import active_children
from tkinter import*
from turtle import bgcolor

#,,,print(btn1.config().keys()),,,to find out options available.
#,,,This is code for Button functions,,,,,,
#,,,button options,,,,,,,,,,,,,,,,,,,,,,,,,
#'''button.config(command=___)no ""needed.
#'''button.config(font=("___",20,"bold"))
#'''button.config(bg="____")
#'''button.config(fg="____")
#'''button.config(activebackground="___")
#'''button.config(activeforground="___")
#'''image=PhotoImage(file="_____")
#'''button.config(image=image)
#'''button.config(compound="top")left,right,bottom,none
#,,,button.config(state=DISABLED)ACTIVE
#,,,button.config(ancor),,sets to one side.
#,,,button.config(boarderwidth)



def onclick(args):#,,,agrs (arguments)means any (button number).gets more than one thing to happen.
    if args == 1:
        print("Button 1 clicked")
        btn1.config(bg="red")
        lb1.config(bg="red") 
        btn2.config(bg="#f0f0f0"),#,,default colour
        lb2.config(bg="#f0f0f0") 
        lb2.config(fg="black")
    if args == 2:
        print("Button 2 clicked")
        btn1.config(bg="#f0f0f0"),#,,default colour
        lb1.config(bg="#f0f0f0")
        btn2.config(bg="red")
        lb2.config(bg="red")
        lb2.config(fg="white")
    
root=Tk()#,,create window.
root.title("Button code Functions when clicked")#,,Title on window.

#,,,create Buttons.
btn1=Button(root,text="Button 1",borderwidth=5,command=lambda:onclick(1))
#,,,Put Button on screen
btn1.pack(side="right")
login_btn=PhotoImage(file='download.png')
btn2=Button(root,image=login_btn,borderwidth=5,compound=LEFT,text="Button 2",command=lambda:onclick(2))
btn2.pack(side="right")



#img_label=Label(image=login_btn)
#img_label.pack(side="right")


#,,,create Labels.
lb1=Label(root,text='LABEL 1',bg="#f0f0f0",relief="ridge",width=8)
lb1.pack(side="right")
lb2=Label(root,text='LABEL 2',bg="#f0f0f0",relief='sunken',width=8)
lb2.pack(side="right")





root.mainloop()#,,keep window showing on screen(constant loop)
