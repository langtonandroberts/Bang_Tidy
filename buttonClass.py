from tkinter import*
root=Tk()
root.title("Button Class")
root.geometry('500x500')



class Application():
    def __init__(self,s1):#,s1 is the (root)
        f1=Frame(s1)#,put frame in s1(root)
        f1.pack()
        self.b1 = Button(s1,text = "click me",command= self.click)
        self.b1.pack()
    
    def click(self):
        print("You clicked the button")
        

obj1=Application(root)#,pass the Application back to root,,for it to run.


        
root.mainloop()
