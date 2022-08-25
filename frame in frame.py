from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x200')

frame = Frame(ws, height=300, width=300, bg='red')
frame.pack()

food = LabelFrame(frame, text='Food', bd=5, relief=RIDGE)
food.grid(row=0, column=0, sticky=W, padx=20, pady=20)

#f=Checkbutton(food, text='test').pack(anchor=W)
f1=Checkbutton(food, text='Pizza').pack(anchor=W)
f2=Checkbutton(food, text='Noodles').pack(anchor=W)
f3=Checkbutton(food, text='Sandwich').pack(anchor=W)
f4=Checkbutton(food, text='eggs').pack(anchor=W)

drinks = LabelFrame(frame, text='Drinks', bd=5, relief=RIDGE)
drinks.grid(row=0, column=1, sticky=E, padx=20, pady=20)

#d=Checkbutton(drinks, text='tester').pack(anchor=W)
d1=Checkbutton(drinks, text='Water').pack(anchor=W)
d2=Checkbutton(drinks, text='Coffee').pack(anchor=W)
d3=Checkbutton(drinks, text='Fanta').pack(anchor=W)
d4=Checkbutton(drinks, text='Bear').pack(anchor=W)

ws.mainloop()