from logging import root
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()

root.title('Langton & Roberts custom bttons')
root.geometry("500x170")

button_1=customtkinter.CTkButton(root,text="Add Folder",width=190,height=40)#corner_radius#compound="right"/left/top/ect.
button_1.pack(pady=20,padx=20)
button_2=customtkinter.CTkButton(master=root,text="Add Item",width=190,height=40)#corner_radius#compound="right"/left/top/ect.
button_2.pack(pady=20,padx=20)



root.mainloop()
