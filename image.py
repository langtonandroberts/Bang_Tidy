from tkinter import *

from PIL import ImageTk,Image
#,,,,,,,,, Creates a window on screen ,,,,,,,,,,,,,,,,,,,,,
root=Tk() 
#,,,,,,,,,,, Name on top of window.(left corner) ,,,,,,,,,,
root.title("HELLO WORLD")

       
root.geometry("550x550") #,,,,defines size of window when ran,,,.

my_image= ImageTk.PhotoImage(Image.open("network.png"))

myLabel=Label(root,image=my_image,bg="red") # could add .grid(row=0, column=0)
myLabel.grid(row=1,column=1)



root.mainloop()# enter everything between this.
