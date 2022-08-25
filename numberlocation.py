from tkinter import *
import webbrowser


ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x400')


new = 1
url = "https://www.bangtidypasta.com"

def openbrowser():
    webbrowser.open(url,new=new)

bg = PhotoImage(file = "Python Codes Projects\Bang_Tidy\logo.png")

canvas = Canvas(
	ws, 
	width = 500,
	height = 400
	)

canvas.pack(fill='both', expand = True)

canvas.create_image(
	0, 
	0, 
	image=bg,
	anchor = "nw"
	)

canvas.create_text(
	250, 
	150, 
	text = 'Bang Tidy Pasta',
	font=('Arial', 50),
	)

btn = Button(
	ws, 
	text = 'GO TO',
	command=openbrowser,
	width=20,
	height=2,
	relief=SOLID,
	font=('arial', 18)
	)

btn_canvas = canvas.create_window(
	100, 
	200,
	anchor = "nw",
	window = btn,
	)


ws.mainloop()
