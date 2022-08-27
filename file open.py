
#https://youtu.be/uQ5BZht9L3A
#https://youtu.be/YgI94IRXySk
#https://youtu.be/Uh2ebFW8OYM
#https://youtu.be/crluPcyuchU
#https://youtu.be/YgI94IRXySk

from tkinter import *
from tkinter import filedialog as fd 
from pathlib import Path 

ws = Tk()
ws.title("File Sellection Code")
ws.geometry("100x100")


# MODE'S
# r read    # readline() brings back 1 line.
# a append  # ,end='' (to remove empty lines)
# w write   # rb & wb (binary code) to be used for pictures jpg
# x Write, fail if file exists
# + Updating (read/write)
# t Text(default)
# b Binary

# write all files with the (with_command)
#example
#stream=open(file_name, mode, buffer_size)#buffer size can be left off as its default.
stream=open('output.txt','w')
print('\nCan I write to this file? ' + str(stream.writable()) + '\n')
print('\nIs this file readable? ' + str(stream.readable()) + '\n')
stream.write('Hello World')
cwd=Path.cwd()
stream=Path.joinpath(cwd, 'stream.txt')

print(stream.exists())




# the open comand.    
# Open is the function to open file
def openf():
    try:
        with open("cinema.csv","r") as f: #(with) is a context manager,,so you do not need to close the file after you open it.
            content = f.read()
        print(content)
    except FileNotFoundError:
        text=None
    
openf()

# opens popup file window
def open_file():
    try:
        filepath = fd.askopenfilename(initialdir="C:\\Users\\Invate\\OneDrive\\Desktop\\Python\\Python cheat sheets\\Python Codes Projects\\Bang_Tidy\\pet notes",
                                    title="Select a file to open",
                                    filetypes=(("text files","*.txt"),("CSV files","*.csv"),("all files","*.*")))
        file=open(filepath,'r')
        print(file.read())
        file.close
    except FileNotFoundError:
        #text=None
        text="you closed the dialog box without choseing a file"
        print(text)
    
# copy a photo file.
def photo_file_copy():
    try:
        with open("file_name.jpg","rb") as rf: #open photo in binery code (use 'rb')
            with open("file_name.jpg","wb") as wf:#copy photo in binery code (use 'wb')
                for line in rf:
                    wf.write(line)
           
    except FileNotFoundError:
        text=None


#photo_file_copy()

error_msg = 'Error!'
Button(text = 'File Open', command = open_file).pack(fill=X)






ws.mainloop()