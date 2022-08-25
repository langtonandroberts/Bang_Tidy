#radiobutton = similar to checkbox, but you can only select one from a group.


from tkinter import *

food = ['Pizza','Hamburger','Hotdog']#index value 0,1,2

def order():
    if (x.get()==0):
        print('You ordered Pizza!')
    elif(x.get()==1):
        print('You ordered a Hamburger!')
    elif(x.get()==2):
        print('You ordered a Hotdog!')
    else:
        print('huh?')
        
window = Tk()

#pizza_image=PhotoImage(file='insert file path or name.png')
#hamburger_image=PhotoImage(file='insert file path or name.png')
#hotdog_image=PhotoImage(file='insert file path or name.png')
#food_images=[pizza_image,hamburger_image,hotdog_image]

x = IntVar()
for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index],#adds text to radio buttons.
                            variable=x,#groups radiobuttons together if they share the same variable
                            value=index,#sasigns each radiobutton a diferent value.(index 0,1,2)
                            padx=25,#adds padding to x axis
                            font=('Impact',20),
                            #image=food_images[index],#adds image to radiobutton.
                            #compound='left',#adds image to the left of text.
                            #indicatoron=0,#eliminates circles and turnd into buttons.
                            anchor=W,
                            width=35,
                            command=order#set command to function
                            )
    radiobutton.pack(anchor=W)

window.mainloop()

