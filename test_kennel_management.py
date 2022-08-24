
from tkinter import ttk 
from tkinter import * 
from datetime import date 
from PIL import Image, ImageTk
from PIL import ImageTk, Image
from random import random 
import random 
from PIL import Image
import tkinter as tk


#Langton_and_Roberts="Langton & RobertS"
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 11)
SMALL_FONT = ("Helvetica", 10)
HEIGHT = 700
WIDTH = 500

class HoverButton(Button):
    """ Button that changes color to activebackground when mouse is over it. """
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.default_Background = self.cget('background')
        self.hover_Background = self.cget('activebackground')
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, e):
        self.config(background=self.hover_Background)

    def on_leave(self, e):
        self.config(background=self.default_Background)


class LangtonAndRoberts(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self,default='home.ico')
        Tk.wm_title(self, 'Langton_and_Roberts')
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        title_text=StringVar()
        title_text.set("Kennel Boarding Managenent System")
        status_bar=Label(self,textvariable=title_text,height=2,relief=FLAT,anchor=CENTER,bg="#e2f723",fg="brown")
        status_bar.pack(fill=X,side=BOTTOM,ipady=2,padx=0)#,expand=True)
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
             
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        #,,Buttons Frame(left),,Center Frame(left),Ribbon Frame(Top),,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        #,,,Ribbon (menu) frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_4=Frame(self,relief=FLAT,bd=0,bg="white",height=6)
        can_4.pack(side='top',anchor=W,fill='x')#,expand=True)
        #,,Frame for Notebook,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_3=Frame(self,relief=FLAT,bg="white")
        can_3.pack(side='left',anchor=W,fill='both',expand=True)  
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")#,background="yellow")
        label.pack()
        
        
        
        #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
        #,,,Home Tab Main Side (Home Page Frames),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        #,,,list of greetings on home page on start up.
        frase_list=["O.M.G!!,,, I can't believe\n",
                    "Shit,,,, I can't believe\n",
                    "Unbelievable,, I can't believe\n"]
        fraze=random.choice(frase_list)#https://youtu.be/XKHEtdqhLK8
        today= date.today()
        f_today=today.strftime('%A \n%B %d \n%Y ')
        day_name=today.strftime('%A')
        #print(day_name)
        if day_name =="Friday":
            today_label=Label(can_3,text=f"Shake your tits,,,\nIt's \n{f_today}",font="helvetica, 70",bg="white",fg="orange",justify=LEFT)
            today_label.grid(row=0,column=0,padx=80,pady=20,sticky=W)#pack(pady=20)
        else:
            today_label=Label(can_3,text=f"{fraze}It's \n{f_today}",font="helvetica, 70",bg="white",fg="orange",justify=LEFT)
            today_label.grid(row=0,column=0,padx=80,pady=20,sticky=W)#pack(pady=20)
            
        #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        #,,,,Left side Buttons linked to Class Button,,,,,,,,,,,,,,,,,,,,,,,,,,,
        button1 = HoverButton(can_2, text="PAGE\nONE",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageOne))
        button1.pack(fill=X,pady=2)#grid(row=2,column=2)#pack()
        button2 = HoverButton(can_2, text="PAGE\nTWO",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageTwo))
        button2.pack(fill=X,pady=2)#grid(row=3,column=1)#pack()
        button3 = HoverButton(can_2, text="PAGE\nTHREE",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageThree))
        button3.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button4 = HoverButton(can_2, text="PAGE\nFOUR",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageFour))
        button4.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        '''button5 = HoverButton(can_2, text="SERVICES",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black")
        button5.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button6 = HoverButton(can_2, text="PET\nINFORMATION",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black")
        button6.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button7 = HoverButton(can_2, text="SELL\nSOMETHING",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black")#lambda: controller.show_frame(PageTwo))
        button7.pack(fill=X,pady=2)#grid(row=3,column=1)#pack()
        button8 = HoverButton(can_2, text="REPORTS",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black")#lambda: controller.show_frame(PageThree))
        button8.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button9 = HoverButton(can_2, text="EMPLOYEES",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black")#lambda: controller.show_frame(PageThree))
        button9.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()'''
        
     
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        #,,, frames left Page One System Info,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        #,,main frame Right side,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        canvas_3=Frame(self,relief=RAISED,bd=0)
        canvas_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")#,background="yellow")
        label.pack()
        button1 = HoverButton(can_2, text="Back to Home Page",font="helvetica 12",activebackground = 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        button1.pack(anchor=W,fill=X)
        #,,,Frames
        top_label_frame=Frame(canvas_3,bd=1)  
        top_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        heading=Label(top_label_frame,text="PAGE ONE",font="bold 30",fg="#347083")
        heading.grid(row=0,column=0,columnspan=3,padx=30,pady=25)
        button_label_frame=Frame(canvas_3,bg="light blue",bd=1)  
        button_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        #,,,Buttons
        button1=HoverButton(button_label_frame,text="BUTTON ONE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button1.grid(row=0,column=0,padx=0,pady=0,ipady=10,ipadx=30)
        button2=HoverButton(button_label_frame,text="BUTTON TWO",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button2.grid(row=0,column=1,padx=0,pady=0,ipady=10,ipadx=30)
        button3=HoverButton(button_label_frame,text="BUTTON THREE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button3.grid(row=0,column=2,padx=0,pady=0,ipady=10,ipadx=30)
        button4=HoverButton(button_label_frame,text="BUTTON FOUR",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button4.grid(row=0,column=3,padx=0,pady=0,ipady=10,ipadx=30)
        button5=HoverButton(button_label_frame,text="BUTTON FIVE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button5.grid(row=0,column=4,padx=0,pady=0,ipady=10,ipadx=30)
        button6=HoverButton(button_label_frame,text="BUTTON SIX",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button6.grid(row=0,column=5,padx=0,pady=0,ipady=10,ipadx=30)


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left and right frames,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        canvas_3=Frame(self,relief=FLAT,bd=0)
        canvas_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        #network_label.grid(row=0,column=0)
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")#,background="yellow")
        label.pack()
        button1 = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        button1.pack(anchor=W,fill=X)
    
        #,,,Frames
        top_label_frame=Frame(canvas_3,bd=1)  
        top_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        heading=Label(top_label_frame,text="PAGE TWO",font="bold 30",fg="#347083")
        heading.grid(row=0,column=0,columnspan=3,padx=30,pady=25)
        button_label_frame=Frame(canvas_3,bg="light blue",bd=1)  
        button_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        #,,,Buttons
        button1=HoverButton(button_label_frame,text="BUTTON ONE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button1.grid(row=0,column=0,padx=0,pady=0,ipady=10,ipadx=30)
        button2=HoverButton(button_label_frame,text="BUTTON TWO",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button2.grid(row=0,column=1,padx=0,pady=0,ipady=10,ipadx=30)
        button3=HoverButton(button_label_frame,text="BUTTON THREE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button3.grid(row=0,column=2,padx=0,pady=0,ipady=10,ipadx=30)
        button4=HoverButton(button_label_frame,text="BUTTON FOUR",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button4.grid(row=0,column=3,padx=0,pady=0,ipady=10,ipadx=30)
        button5=HoverButton(button_label_frame,text="BUTTON FIVE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button5.grid(row=0,column=4,padx=0,pady=0,ipady=10,ipadx=30)
        button6=HoverButton(button_label_frame,text="BUTTON SIX",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button6.grid(row=0,column=5,padx=0,pady=0,ipady=10,ipadx=30)


class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        button1 = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        button1.pack(anchor=W,fill=X)


class PageFour(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        button1 = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        button1.pack(anchor=W,fill=X)


app = LangtonAndRoberts()

# ,,, make start up screen fit any monitor ,,,,,,,
width_value=app.winfo_screenwidth()
height_value=app.winfo_screenheight()
app.geometry(f"{width_value}x{height_value}+0+0")


app.mainloop()
