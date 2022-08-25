from tkinter import*

'''this file shows how you can 
make a Class for a button then call it 
to be used later'''

root=Tk()
root.title("Hover Button Class")
root.geometry("550x550")


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



button = HoverButton(root, padx=7, pady=7, relief=RIDGE,activebackground= 'blue', text='SAVE')
button.grid(row=0, column=0, sticky='news')
#button.pack()


root.mainloop()



