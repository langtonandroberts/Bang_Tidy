from tkinter import*
import pyttsx3



#,, docs can be found at pypi.org
root=Tk()
root.title('Text to speech')
root.geometry('800x500')

def talk():
    engine=pyttsx3.init()
    #engine.say(my_entry.get())
    #engine.say(my_entry2.get())
    #engine.say(my_entry3.get())
    engine.say(f''' you have chosen, employee reference number
               {my_entry.get()}, {my_entry2.get()},{my_entry3.get()}to be deleted from all records,
               if this is correct, select yes,
               alternatively, if this was a error in any way, select no..''')
    engine.runAndWait()
    my_entry.delete(0,END)
    my_entry2.delete(0,END)
    my_entry3.delete(0,END)
    

my_entry=Entry(root)
my_entry.pack(pady=20)
my_entry2=Entry(root)
my_entry2.pack(pady=20)
my_entry3=Entry(root)
my_entry3.pack(pady=20)
my_button=Button(root,text="Speak",command=talk)
my_button.pack()



root,mainloop()
